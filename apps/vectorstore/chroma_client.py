"""
ChromaDB vector database client.
"""

import chromadb

from configs.settings import settings

# Persistent local ChromaDB storage
client = chromadb.PersistentClient(path=settings.CHROMA_DB_DIR)

# Financial article collection
collection = client.get_or_create_collection(name="financial_news")
