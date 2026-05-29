import asyncio

from apps.db.session import AsyncSessionLocal
from apps.repositories.news_repository import (
    NewsRepository,
)
from apps.services.ingestion_service import (
    IngestionService,
)


async def test_ingestion():

    async with AsyncSessionLocal() as db:
        repository = NewsRepository(db)

        service = IngestionService(repository)

        result = await service.ingest_articles()

        print(f"Stored articles: {result}")


asyncio.run(test_ingestion())
