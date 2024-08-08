from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from core.models import db_helper, UserCard
from core.schemas import UserCardCreate, UserCardRead
from typing import List


router = APIRouter(tags=["UserCard"])


@router.post("", response_model=UserCardRead)
async def create_user_card(
    user_card_create: UserCardCreate,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    user_card = UserCard(**user_card_create.dict())
    
    session.add(user_card)
    
    try:
        await session.commit()
        await session.refresh(user_card)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=400, detail="User or Card not found or UserCard already exists")
    
    return user_card


@router.delete("/{user_card_id}", response_model=UserCardRead)
async def delete_user_card(
    user_card_id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(UserCard).where(UserCard.id == user_card_id)
    result = await session.scalars(stmt)
    user_card = result.first()

    if not user_card:
        raise HTTPException(status_code=404, detail="UserCard not found")

    await session.delete(user_card)
    await session.commit()

    return user_card


@router.get("/{user_card_id}", response_model=UserCardRead)
async def get_user_card_by_id(
    user_card_id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(UserCard).where(UserCard.id == user_card_id)
    result = await session.scalars(stmt)
    user_card = result.first()

    if not user_card:
        raise HTTPException(status_code=404, detail="UserCard not found")

    return user_card


@router.get("/user/{user_id}", response_model=List[UserCardRead])
async def get_user_cards_by_user_id(
    user_id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(UserCard).where(UserCard.user_id == user_id)
    result = await session.scalars(stmt)
    user_cards = result.all()
    
    return user_cards


@router.get("/card/{card_id}", response_model=List[UserCardRead])
async def get_user_cards_by_card_id(
    card_id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(UserCard).where(UserCard.card_id == card_id)
    result = await session.scalars(stmt)
    user_cards = result.all()
    
    return user_cards


@router.get("", response_model=List[UserCardRead])
async def get_all_user_cards(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(UserCard).order_by(UserCard.id)
    result = await session.scalars(stmt)
    user_cards = result.all()
    
    return user_cards
