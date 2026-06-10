from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.session import get_db
from apps.services.system_service import SystemService

router = APIRouter(
    prefix="/system",
    tags=["System"],
)


@router.get("/health")
async def health():
    """
    Application health check.
    """

    return {
        "status": "healthy",
        "database": "healthy",
    }


@router.get("/status")
async def status(
    db: AsyncSession = Depends(get_db),
):
    """
    Full system status.
    """

    service = SystemService(db)

    database_ok = await service.database_health()

    return {
        "api": "healthy",
        "database": ("healthy" if database_ok else "unhealthy"),
    }


@router.get("/metrics")
async def metrics(
    db: AsyncSession = Depends(get_db),
):
    service = SystemService(db)

    return {"articles": (await service.article_count())}
