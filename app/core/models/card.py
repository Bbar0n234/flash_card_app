from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Card(Base):
    __tablename__ = 'cards'
    id = Column(Integer, primary_key=True, index=True)
    english = Column(String, index=True)
    russian = Column(String)
    category = Column(String, nullable=True)
    difficulty = Column(String, nullable=True)
    learning_progress = relationship('LearningProgress', back_populates='card')