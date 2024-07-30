from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class LearningProgress(Base):
    __tablename__ = 'learning_progress'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    card_id = Column(Integer, ForeignKey('cards.id'))
    right_answers = Column(Integer, default=0)
    wrong_answers = Column(Integer, default=0)
    user = relationship('User', back_populates='learning_progress')
    card = relationship('Card', back_populates='learning_progress')