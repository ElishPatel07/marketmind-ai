from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from apps.db.session import get_db
from apps.repositories.chat_repository import (
    ChatRepository,
)
from apps.schemas.chat import (
    ChatRequest,
)
from apps.services.chat_service import (
    ChatService,
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("/query")
async def query_chat(
    payload: ChatRequest,
    db: AsyncSession = Depends(get_db),
):
    repository = ChatRepository(db)

    service = ChatService(repository)

    return await service.chat(
        session_key=payload.session_id,
        query=payload.query,
    )
