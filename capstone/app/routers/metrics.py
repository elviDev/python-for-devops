from fastapi import APIRouter, HTTPException

from app.services.metrics_service import get_system_metrics


router = APIRouter(tags=["metrics"])


@router.get("/metrics")
def get_metrics(cpu_threshold: float = 85.0):
    """Return current system metrics."""
    try:
        return get_system_metrics(cpu_threshold)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Could not read system metrics: {exc}",
        ) from exc