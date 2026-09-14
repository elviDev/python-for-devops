from pydantic import BaseModel


class AIAnalyzeRequest(BaseModel):
    file: str | None = None


class AIAnalyzeResponse(BaseModel):
    log_file: str
    counts: dict[str, int]
    analysis: str
    model: str