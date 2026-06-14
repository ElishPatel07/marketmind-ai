from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.session import get_db
from apps.repositories.portfolio_repository import PortfolioRepository
from apps.schemas.portfolio import PortfolioCreate
from apps.services.portfolio_service import PortfolioService

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"],
)


@router.post("/")
async def create_portfolio(
    request: PortfolioCreate,
    db: AsyncSession = Depends(get_db),
):
    repository = PortfolioRepository(db)

    service = PortfolioService(repository)

    portfolio = await service.create_portfolio(
        request.name,
        request.holdings,
    )

    return {
        "portfolio_id": portfolio.id,
        "name": portfolio.name,
    }


@router.get("/{portfolio_id}/report")
async def portfolio_report(
    portfolio_id: int,
    db: AsyncSession = Depends(get_db),
):
    repository = PortfolioRepository(db)

    service = PortfolioService(repository)

    return await service.generate_report(portfolio_id)
