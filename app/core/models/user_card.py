from sqlalchemy import event, DDL, Integer, Column, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from .base import Base


class UserCard(Base):
    __tablename__ = 'user_card'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    card_id = Column(Integer, ForeignKey('cards.id'))

    user = relationship('Users', back_populates='user_card')
    card = relationship('Cards', back_populates='user_card')
    answers = relationship('Answers', back_populates='user_card', uselist=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'card_id', name='uq_user_card'),
    )
