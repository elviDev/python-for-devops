from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.schemas.ai import AIAnalyzeRequest, AIAnalyzeResponse
from app.services.ai_service import analyze_logs_with_ai


router = APIRouter(prefix="/ai", tags=["ai"])

BASE_DIR = Path(__file__).resolve().parents[2]
LOG_DIR = BASE_DIR / "sample_logs"
DEFAULT_LOG = LOG_DIR / "app.log"


def resolve_log_path(file: str | None) -> Path:
    """Resolve a log filename without allowing access outside LOG_DIR."""
    if not file:
        return DEFAULT_LOG

    requested_path = Path(file)

    if requested_path.is_absolute():
        raise ValueError("Only log filenames inside the log directory are allowed.")

    candidate = (LOG_DIR / requested_path).resolve()

    if candidate != LOG_DIR and LOG_DIR not in candidate.parents:
        raise ValueError("Log file must be inside the log directory.")

    if candidate.suffix.lower() != ".log":
        raise ValueError("Only .log files are allowed.")

    return candidate


@router.post(
    "/analyze",
    response_model=AIAnalyzeResponse,
)
def analyze_with_ai(request: AIAnalyzeRequest):
    """Analyze an approved log file using the local AI agent."""
    try:
        path = resolve_log_path(request.file)
        return analyze_logs_with_ai(path)

    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    except ConnectionError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"AI service unavailable: {exc}",
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail=f"AI analysis failed: {exc}",
        ) from exc