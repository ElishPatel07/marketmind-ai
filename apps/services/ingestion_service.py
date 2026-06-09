"""
Financial news ingestion service.
"""

from dateutil import parser
from loguru import logger

from apps.ingestion.rss_ingestion import (
    deduplicate_articles,
    fetch_rss_articles,
)
from apps.repositories.news_repository import (
    NewsRepository,
)
from apps.schemas.news import (
    NewsArticleCreate,
)
from apps.services.intelligence_service import (
    IntelligenceService,
)
from apps.vectorstore.embedding_service import (
    EmbeddingService,
)


class IngestionService:
    """
    Financial news ingestion workflow.
    """

    def __init__(
        self,
        repository: NewsRepository,
    ):

        self.repository = repository
        self.intelligence_service = IntelligenceService()
        self.embedding_service = EmbeddingService()

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

        stored_articles = 0

        for article in unique_articles:
            existing_article = await self.repository.article_exists(article["link"])

            if existing_article:
                continue

            # Skip invalid articles
            if not article["content"] or len(article["content"]) < 20:
                continue

            analysis = await self.intelligence_service.analyze_article(
                article["content"]
            )

            payload = NewsArticleCreate(
                title=article["title"],
                source=article["source"],
                content=article["content"],
                published_at=parser.parse(article["published_at"]),
                article_url=article["link"],
                sentiment=analysis["sentiment"],
            )

            logger.info(f"Persisting article: {article['title']}")

            try:
                stored_article = await self.repository.create_article(payload)

                # Generate semantic embedding
                await self.embedding_service.generate_embedding(
                    article_id=stored_article.id,
                    content=stored_article.content,
                )

                stored_articles += 1

            except Exception as exc:
                logger.error(f"Failed to persist article: {exc}")

        logger.info(f"Persisted {stored_articles} new articles")

        return stored_articles
