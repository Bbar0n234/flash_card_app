from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from typing import List

from .base import Base


class Users(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False)

    user_card = relationship('UserCard', back_populates='user')
