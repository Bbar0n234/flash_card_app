from sqlalchemy import Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base

class LearningProgress(Base):
    __tablename__ = 'learning_progress'
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    card_id: Mapped[int] = mapped_column(Integer, ForeignKey('cards.id'))
    right_answers: Mapped[int] = mapped_column(Integer, default=0)
    wrong_answers: Mapped[int] = mapped_column(Integer, default=0)
    
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'card_id', name='pk_user_card'),
    )
    
    user: Mapped["Users"] = relationship('Users', back_populates='learning_progress')
    card: Mapped["Cards"] = relationship('Cards', back_populates='learning_progress')
