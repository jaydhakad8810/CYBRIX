from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.models.analysis import AnalysisResponse, LinkAnalysisRequest, MessageAnalysisRequest
from app.services.analysis_service import AnalysisService
from app.services.decision_engine import DecisionEngine


router = APIRouter()
analysis_service = AnalysisService()
decision_engine = DecisionEngine()


class UnifiedAnalysisRequest(BaseModel):
    url: str | None = Field(default=None, min_length=1, description="Optional URL to analyze.")
    message: str | None = Field(default=None, min_length=1, description="Optional message to analyze.")


@router.post("")
def analyze(payload: UnifiedAnalysisRequest) -> dict:
    """Unified endpoint that combines link and message analysis into a final decision."""
    link_result = None
    message_result = None

    if payload.url:
        link_result = analysis_service.analyze_link(payload.url).model_dump()

    if payload.message:
        message_result = analysis_service.analyze_message(payload.message).model_dump()

    return decision_engine.generate_decision(
        {
            "link": link_result,
            "message": message_result,
        }
    )


@router.post("/link", response_model=AnalysisResponse)
def analyze_link(payload: LinkAnalysisRequest) -> AnalysisResponse:
    """Rule-based endpoint for link analysis."""
    return analysis_service.analyze_link(payload.url)


@router.post("/message", response_model=AnalysisResponse)
def analyze_message(payload: MessageAnalysisRequest) -> AnalysisResponse:
    """Rule-based endpoint for phishing and scam message analysis."""
    return analysis_service.analyze_message(payload.message)
