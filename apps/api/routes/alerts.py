from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.session import get_db
from apps.repositories.alert_repository import AlertRepository

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get("/")
async def alerts(
    db: AsyncSession = Depends(get_db),
):
    repository = AlertRepository(db)

    return await repository.get_alerts()
