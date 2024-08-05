from sqlalchemy import Integer, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .base import Base


class UserCard(Base):
    __tablename__ = 'user_card'
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    card_id: Mapped[int] = mapped_column(Integer, ForeignKey('cards.id'))

    user = relationship('Users', back_populates='user_card')
    card = relationship('Cards', back_populates='user_card')
    user_card_answers = relationship('UserCardAnswers', back_populates='user_card', uselist=False)

    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'card_id', name='pk_user_card'),
    )