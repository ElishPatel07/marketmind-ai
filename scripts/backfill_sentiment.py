import asyncio

from sqlalchemy import select

from apps.db.models.news_article import NewsArticle
from apps.db.session import AsyncSessionLocal
from apps.services.intelligence_service import (
    IntelligenceService,
)


async def main():

    intelligence = IntelligenceService()

    async with AsyncSessionLocal() as db:
        result = await db.execute(select(NewsArticle))

        articles = result.scalars().all()

        for article in articles:
            if article.sentiment:
                continue

            analysis = await intelligence.analyze_article(article.content)

            article.sentiment = analysis["sentiment"]

            print(
                article.id,
                article.sentiment,
            )

        await db.commit()


asyncio.run(main())
