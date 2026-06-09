from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.models.news_article import (
    NewsArticle,
)


class IntelligenceRepository:
    def __init__(
        self,
        db: AsyncSession,
    ):
        self.db = db

    async def get_sentiment_counts(
        self,
    ):
        """
        Get sentiment distribution.
        """

        result = await self.db.execute(
            select(
                NewsArticle.sentiment,
                func.count(),
            ).group_by(NewsArticle.sentiment)
        )

        return result.all()

    async def get_recent_articles(
        self,
        limit: int = 10,
    ):
        """
        Get recent articles.
        """

        result = await self.db.execute(
            select(NewsArticle).order_by(NewsArticle.id.desc()).limit(limit)
        )

        return result.scalars().all()
