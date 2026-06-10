from loguru import logger

from apps.db.session import (
    AsyncSessionLocal,
)
from apps.repositories.news_repository import (
    NewsRepository,
)
from apps.services.ingestion_service import (
    IngestionService,
)


async def run_ingestion_job():
    """
    Scheduled ingestion.
    """

    logger.info("Running scheduled ingestion")

    async with AsyncSessionLocal() as db:
        repository = NewsRepository(db)

        service = IngestionService(repository)

        await service.ingest_articles()
