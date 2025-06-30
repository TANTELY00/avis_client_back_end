from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.services.review_service import create_review
from app.db import get_async_session
from app.schemas.review import ReviewCreate

router = APIRouter()

@router.post("/reviews/")
async def add_review(review: ReviewCreate, db: AsyncSession = Depends(get_async_session)):
    result = await create_review(db, review.text, review.client_name, review.client_email)
    return result
