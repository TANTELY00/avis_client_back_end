from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.review import ReviewCreate
from app.db import get_db
from app.services.review_service import create_review

router = APIRouter()

@router.post("/")
async def submit_review(payload: ReviewCreate, db: AsyncSession = Depends(get_db)):
    result = await create_review(db, payload.text)
    return result
