from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.models.portfolio import Portfolio
from apps.db.models.portfolio_holding import PortfolioHolding


class PortfolioRepository:
    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def create_portfolio(
        self,
        name: str,
    ):
        portfolio = Portfolio(name=name)

        self.db.add(portfolio)

        await self.db.commit()

        await self.db.refresh(portfolio)

        return portfolio

    async def get_portfolio(
        self,
        portfolio_id: int,
    ):
        result = await self.db.execute(
            select(Portfolio).where(Portfolio.id == portfolio_id)
        )

        return result.scalar_one_or_none()

    async def add_holding(
        self,
        portfolio_id: int,
        ticker: str,
    ):
        holding = PortfolioHolding(
            portfolio_id=portfolio_id,
            ticker=ticker,
        )

        self.db.add(holding)

        await self.db.commit()

        return holding

    async def get_holdings(
        self,
        portfolio_id: int,
    ):
        """
        Get portfolio holdings.
        """

        result = await self.db.execute(
            select(PortfolioHolding).where(
                PortfolioHolding.portfolio_id == portfolio_id
            )
        )

        return result.scalars().all()
