from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base


class Answers(Base):
    __tablename__ = 'answers'
    
    user_card_id: Mapped[int] = mapped_column(Integer, ForeignKey('user_card.id'), primary_key=True)
    right_answers: Mapped[int] = mapped_column(Integer, default=0)
    wrong_answers: Mapped[int] = mapped_column(Integer, default=0)
    
    user_card: Mapped["UserCard"] = relationship("UserCard", back_populates="answers")

