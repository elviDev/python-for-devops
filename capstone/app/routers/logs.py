from pathlib import Path

from fastapi import APIRouter, HTTPException

from app.services.log_service import analyze_log_file


router = APIRouter(tags=["logs"])

DEFAULT_LOG = Path(__file__).resolve().parents[2] / "sample_logs" / "app.log"


@router.get("/logs")
def get_log_summary(file: str | None = None):
    """Analyze a log file and return deterministic log statistics."""
    path = Path(file) if file else DEFAULT_LOG

    try:
        return analyze_log_file(path)
    except FileNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except OSError as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to read log file: {exc}",
        ) from exc