"""
Centralized Groq client.

All LLM interactions should use this client.
"""

from groq import Groq

from configs.settings import settings

client = Groq(
    api_key=settings.GROQ_API_KEY,
)
