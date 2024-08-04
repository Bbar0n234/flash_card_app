from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Users
from core.schemas import UserCreate, UserRead

from typing import List

router = APIRouter(tags=["Users"])

@router.get("", response_model=List[UserRead])
async def get_all_users(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Users).order_by(Users.id)
    result = await session.scalars(stmt)
    users = result.all()
    return users

@router.post("", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_create: UserCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    # Проверка существования пользователя с таким же username или email
    stmt = select(Users).where((Users.username == user_create.username) | (Users.email == user_create.email))
    result = await session.execute(stmt)
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already registered")

    # Если пользователь не существует, создаем нового
    user = Users(**user_create.dict())
    session.add(user)
    
    await session.commit()
    await session.refresh(user)

    return user

@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    stmt = select(Users).where(Users.id == user_id)
    result = await session.scalars(stmt)
    user = result.one_or_none()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user

@router.delete("/{user_id}", response_model=UserRead)
async def delete_user(
    user_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    stmt = select(Users).where(Users.id == user_id)
    result = await session.scalars(stmt)
    user = result.one_or_none()
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    await session.delete(user)
    await session.commit()
    
    return user
