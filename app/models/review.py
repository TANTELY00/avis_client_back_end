from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime  # <-- cet import est indispensable
from app.db import Base

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    # date = Column(DateTime, default=datetime.utcnow, nullable=False) 

    sentiment_result = relationship("SentimentResult", back_populates="review", uselist=False)
