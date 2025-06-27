from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", backref="reviews")
