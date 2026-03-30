from fastapi import APIRouter

from app.models.analysis import AnalysisResponse, LinkAnalysisRequest, MessageAnalysisRequest
from app.services.analysis_service import AnalysisService


router = APIRouter()
analysis_service = AnalysisService()


@router.post("/link", response_model=AnalysisResponse)
def analyze_link(payload: LinkAnalysisRequest) -> AnalysisResponse:
    """Rule-based endpoint for link analysis."""
    return analysis_service.analyze_link(payload.url)


@router.post("/message", response_model=AnalysisResponse)
def analyze_message(payload: MessageAnalysisRequest) -> AnalysisResponse:
    """Placeholder endpoint for message analysis."""
    return analysis_service.analyze_message(payload.content)
