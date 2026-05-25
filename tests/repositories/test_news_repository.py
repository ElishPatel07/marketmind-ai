"""
Repository layer tests.
"""

import pytest

from apps.repositories import (
    NewsRepository,
)
from apps.schemas.news import (
    NewsArticleCreate,
)


@pytest.mark.asyncio
async def test_create_article_repository(
    db_session,
):
    """
    Validate repository article creation.
    """

    repository = NewsRepository(db_session)

    payload = NewsArticleCreate(
        title="NVIDIA expands AI chips",
        source="Bloomberg",
        content=("NVIDIA announced new AI infrastructure chips."),
    )

    article = await repository.create_article(payload)

    assert article.id is not None

    assert article.title == payload.title

    assert article.source == payload.source
