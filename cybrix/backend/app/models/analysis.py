from pydantic import BaseModel, Field


class MessageAnalysisRequest(BaseModel):
    message: str = Field(..., min_length=1, description="Message content to analyze.")


class LinkAnalysisRequest(BaseModel):
    url: str = Field(..., min_length=1, description="URL to analyze.")


class AnalysisResponse(BaseModel):
    risk: int
    reason: list[str]
    action: str
