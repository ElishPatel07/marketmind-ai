"""
Production routes for financial news APIs.
"""

from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.session import get_db
from apps.repositories import NewsRepository
from apps.schemas.news import (
    NewsArticleCreate,
    NewsArticleResponse,
)
from apps.services import NewsService
from apps.tasks.news_tasks import (
    process_news_article,
)

# Router for financial news endpoints
router = APIRouter(
    prefix="/news",
    tags=["Financial News"],
)


@router.post(
    "/",
    response_model=NewsArticleResponse,
    status_code=201,
)
async def create_article(
    payload: NewsArticleCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    """
    Create financial news article.
    """

    repository = NewsRepository(db)

    service = NewsService(repository)

    article = await service.create_article(payload)

    # Add background task for processing
    background_tasks.add_task(process_news_article, article_id=article.id)

    return article


@router.get(
    "/{article_id}",
    response_model=NewsArticleResponse,
)
async def get_news_article(
    article_id: int,
    db: AsyncSession = Depends(get_db),
):
    """
    Retrieve financial news article by ID.
    """

    repository = NewsRepository(db)

    service = NewsService(repository)

    article = await service.get_article(article_id)

    return article


@router.get(
    "/",
    response_model=list[NewsArticleResponse],
)
async def list_news_articles(
    db: AsyncSession = Depends(get_db),
):
    """
    Retrieve all financial news articles.
    """

    repository = NewsRepository(db)

    service = NewsService(repository)

    articles = await service.list_articles()

    return articles
