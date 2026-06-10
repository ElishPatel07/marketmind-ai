from sqlalchemy import func, select, text

from apps.db.models.news_article import NewsArticle


class SystemService:
    def __init__(
        self,
        db,
    ):
        self.db = db

    async def database_health(
        self,
    ):
        """
        Verify database connection.
        """

        await self.db.execute(text("SELECT 1"))

        return True

    async def article_count(
        self,
    ):
        result = await self.db.execute(select(func.count(NewsArticle.id)))

        return result.scalar()
