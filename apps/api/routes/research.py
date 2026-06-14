from fastapi import APIRouter

from apps.agents.research_agent import (
    ResearchAgent,
)
from apps.schemas.research import (
    ResearchRequest,
    ResearchResponse,
)

router = APIRouter(
    prefix="/research",
    tags=["Research"],
)


@router.post(
    "/analyze",
    response_model=ResearchResponse,
)
async def analyze(
    request: ResearchRequest,
):
    agent = ResearchAgent()

    return await agent.analyze(request.query)
