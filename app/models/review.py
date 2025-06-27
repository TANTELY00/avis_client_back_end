from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db import Base  # <- Import important

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)

    sentiment_result = relationship("SentimentResult", back_populates="review", uselist=False)
