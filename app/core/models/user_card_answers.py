from sqlalchemy import Integer, PrimaryKeyConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base


class UserCardAnswers(Base):
    __tablename__ = 'user_card_answers'
    
    user_id: Mapped[int] = mapped_column(Integer)
    card_id: Mapped[int] = mapped_column(Integer)
    right_answers: Mapped[int] = mapped_column(Integer, default=0)
    wrong_answers: Mapped[int] = mapped_column(Integer, default=0)
    
    # Composite primary key constraint
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'card_id', name='pk_user_card_answers'),
        ForeignKeyConstraint(['user_id', 'card_id'], ['user_card.user_id', 'user_card.card_id']),
    )

    # Relationships
    user_card: Mapped["UserCard"] = relationship("UserCard", back_populates="user_card_answers")
