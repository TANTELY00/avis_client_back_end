from sqlalchemy import Column, Integer, String, ForeignKey
from app.db import Base

class SentimentResult(Base):
    __tablename__ = "sentiment_results"
    id = Column(Integer, primary_key=True, index=True)
    review_id = Column(Integer, ForeignKey("reviews.id"))
    sentiment = Column(String, nullable=False)
