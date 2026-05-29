"""
Embedding generation service.
"""

from loguru import logger
from sentence_transformers import (
    SentenceTransformer,
)

from apps.vectorstore.chroma_client import (
    collection,
)

# Lightweight embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


class EmbeddingService:
    """
    Semantic embedding workflow.
    """

    async def generate_embedding(
        self,
        article_id: int,
        content: str,
    ):
        """
        Generate semantic embedding
        and store in ChromaDB.
        """

        logger.info(f"Generating embedding for article_id={article_id}")

        embedding = model.encode(content).tolist()

        collection.add(
            ids=[str(article_id)],
            embeddings=[embedding],
            documents=[content],
            metadatas=[
                {
                    "article_id": article_id,
                }
            ],
        )

        logger.info(f"Stored embedding for article_id={article_id}")

    async def semantic_search(
        self,
        query: str,
        limit: int = 5,
    ):
        """
        Perform semantic similarity search.
        """

        logger.info(f"Semantic search query: {query}")

        query_embedding = model.encode(query).tolist()

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=limit,
        )

        return results
