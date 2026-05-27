"""
RSS ingestion pipeline.
"""

from datetime import datetime

import feedparser
from loguru import logger

RSS_FEEDS = [
    "https://feeds.finance.yahoo.com/rss/2.0/headline",
    "https://www.marketwatch.com/rss/topstories",
    "https://www.investing.com/rss/news.rss",
]


async def fetch_rss_articles():
    """
    Fetch financial news articles
    from RSS feeds.
    """

    articles = []

    logger.info("Starting RSS ingestion")

    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)

            logger.info(f"Fetched RSS feed: {feed_url}")

            for entry in feed.entries:
                article = {
                    "title": entry.get(
                        "title",
                        "",
                    ),
                    "source": feed.feed.get(
                        "title",
                        "Unknown",
                    ),
                    "content": entry.get(
                        "summary",
                        "",
                    ),
                    "published_at": (
                        entry.get(
                            "published",
                            str(datetime.utcnow()),
                        )
                    ),
                    "link": entry.get(
                        "link",
                        "",
                    ),
                }

                articles.append(article)

        except Exception as exc:
            logger.error(f"RSS ingestion failed: {feed_url} error={exc}")

    logger.info(f"Fetched {len(articles)} articles")

    return articles


def deduplicate_articles(
    articles,
):
    """
    Remove duplicate articles
    by title.
    """

    seen_titles = set()

    unique_articles = []

    for article in articles:
        title = article["title"].strip().lower()

        if title not in seen_titles:
            seen_titles.add(title)

            unique_articles.append(article)

    return unique_articles
