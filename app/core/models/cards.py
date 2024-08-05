from sqlalchemy import Integer, String, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .base import Base

from typing import Optional


class Cards(Base):
    __tablename__ = 'cards'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    english: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    russian: Mapped[str] = mapped_column(String(100), nullable=False)
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.id'), nullable=True)
    difficulty: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    __table_args__ = (
        CheckConstraint('difficulty IS NULL OR difficulty IN (1, 2, 3)', name='check_difficulty'),
    )

    category = relationship('Categories')
    user_card = relationship('UserCard', back_populates='card')


