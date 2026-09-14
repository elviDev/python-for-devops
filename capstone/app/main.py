from fastapi import FastAPI

from app.routers import ai, aws, logs, metrics


app = FastAPI(
    title="DevOps Intelligence API",
    description=(
        "A Python DevOps service for log analysis, system metrics, "
        "AWS resource visibility, and AI-assisted investigation."
    ),
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "name": "DevOps Intelligence API",
        "version": app.version,
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


app.include_router(logs.router)
app.include_router(metrics.router)
app.include_router(aws.router)
app.include_router(ai.router)