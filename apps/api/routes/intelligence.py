from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.session import get_db
from apps.repositories.intelligence_repository import (
    IntelligenceRepository,
)
from apps.services.intelligence_service import (
    IntelligenceService,
)

router = APIRouter(
    prefix="/intelligence",
    tags=["Intelligence"],
)


@router.get("/summary")
async def get_summary(
    db: AsyncSession = Depends(get_db),
):

    repository = IntelligenceRepository(db)

    service = IntelligenceService(repository)

    return await service.get_summary()
