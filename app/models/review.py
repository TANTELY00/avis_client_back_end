from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"))  # 🔥 association avec Client

    sentiment_result = relationship("SentimentResult", back_populates="review", uselist=False)
    client = relationship("Client", back_populates="reviews")
