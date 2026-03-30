from pydantic import BaseModel, Field


class MessageAnalysisRequest(BaseModel):
    content: str = Field(..., min_length=1, description="Text or URL to analyze.")


class LinkAnalysisRequest(BaseModel):
    url: str = Field(..., min_length=1, description="URL to analyze.")


class AnalysisResponse(BaseModel):
    risk: int
    reason: list[str]
    action: str
