"""
Financial news ingestion service.
"""

from loguru import logger

from apps.ingestion.rss_ingestion import (
    deduplicate_articles,
    fetch_rss_articles,
)


class IngestionService:
    """
    Financial news ingestion workflow.
    """

    async def ingest_articles(
        self,
    ):
        """
        Fetch and normalize articles.
        """

        logger.info("Starting ingestion workflow")

        articles = await fetch_rss_articles()

        unique_articles = deduplicate_articles(articles)

        logger.info(f"Normalized {len(unique_articles)} articles")

        return unique_articles
