from pydantic import BaseModel

class ReviewCreate(BaseModel):
    text: str

class ReviewResponse(BaseModel):
    review_id: int
    sentiment: str
    theme: str
    original_review: str
    suggestion: str
