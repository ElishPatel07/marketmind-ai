from apps.agents.research_agent import ResearchAgent
from apps.repositories.portfolio_repository import PortfolioRepository


class PortfolioService:
    def __init__(
        self,
        repository: PortfolioRepository,
    ):

        self.repository = repository
        self.research_agent = ResearchAgent()

    async def create_portfolio(
        self,
        name: str,
        holdings: list[str],
    ):
        portfolio = await self.repository.create_portfolio(name)

        for ticker in holdings:
            await self.repository.add_holding(
                portfolio.id,
                ticker,
            )

        return portfolio

    async def generate_report(
        self,
        portfolio_id: int,
    ):
        portfolio = await self.repository.get_portfolio(portfolio_id)
        holdings = await self.repository.get_holdings(portfolio_id)
        tickers = [holding.ticker for holding in holdings]
        query = "Analyze portfolio: " + ", ".join(tickers)
        analysis = await self.research_agent.analyze(query)

        return {
            "portfolio": portfolio.name,
            "holdings": tickers,
            "outlook": analysis["outlook"],
            "risks": analysis["risks"],
            "opportunities": analysis["opportunities"],
            "report": analysis["report"],
        }
