"""
Service layer tests.
"""

from unittest.mock import AsyncMock

import pytest

from apps.core.exceptions import (
    DatabaseOperationException,
)
from apps.schemas.news import (
    NewsArticleCreate,
)
from apps.services.news_service import (
    NewsService,
)
from apps.tasks.news_tasks import (
    process_news_article,
)


@pytest.mark.asyncio
async def test_create_article_service():
    """
    Validate service layer article creation.
    """

    mock_repository = AsyncMock()

    payload = NewsArticleCreate(
        title="Microsoft expands AI cloud",
        source="Reuters",
        content=("Microsoft announced expanded AI cloud services."),
    )

    mock_article = AsyncMock()

    mock_article.id = 1
    mock_article.title = payload.title
    mock_article.source = payload.source
    mock_article.content = payload.content

    mock_repository.create_article.return_value = mock_article

    service = NewsService(repository=mock_repository)

    result = await service.create_article(payload)

    assert result.title == payload.title

    assert result.source == payload.source

    mock_repository.create_article.assert_awaited_once()


@pytest.mark.asyncio
async def test_create_article_service_failure():
    """
    Validate service failure handling.
    """

    mock_repository = AsyncMock()

    payload = NewsArticleCreate(
        title="Invalid article",
        source="Reuters",
        content=("This is a failure scenario used for service testing."),
    )

    mock_repository.create_article.side_effect = Exception("Database failure")

    service = NewsService(repository=mock_repository)

    with pytest.raises(DatabaseOperationException):
        await service.create_article(payload)


@pytest.mark.asyncio
async def test_background_task():
    """
    Validate async background task execution.
    """

    await process_news_article(1)
