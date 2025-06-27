from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.review_service import create_review
from app.db import get_async_session

router = APIRouter()

@router.post("/reviews/")
async def post_review(text: str, db: AsyncSession = Depends(get_async_session)):
    response = await create_review(db, text)
    return response
