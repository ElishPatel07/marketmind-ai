"""
Service layer for financial news workflows.

Services contain:
- business logic
- orchestration
- workflow management
- cross repository coordination

Services SHOULD NOT:
- contain raw SQL
- directly manage persistence details

Repositories handle persistence.
Services handle workflows.
"""

from apps.repositories.news_repository import NewsRepository
from apps.schemas.news import (
    NewsArticleCreate,
)


class NewsService:
    """
    Service layer for financial news operations.
    """

    def __init__(
        self,
        repository: NewsRepository,
    ):
        """
        Service initialized with repository dependency.
        """

        self.repository = repository

    async def create_article(
        self,
        payload: NewsArticleCreate,
    ):
        """
        Create financial news article workflow.

        Later this workflow may include:
        - duplicate detection
        - sentiment analysis
        - embeddings generation
        - event extraction
        - caching
        - notifications
        """

        # Future business rules can live here
        # before persistence occurs

        article = await self.repository.create_article(payload)

        return article

    async def get_article(
        self,
        article_id: int,
    ):
        """
        Retrieve single article workflow.
        """

        article = await self.repository.get_article_by_id(article_id)

        return article

    async def list_articles(
        self,
    ):
        """
        Retrieve all articles workflow.
        """

        articles = await self.repository.get_all_articles()

        return articles
