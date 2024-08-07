from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Cards, Categories
from core.schemas import CardRead, CardCreate, CardUpdate

from typing import List, Optional


router = APIRouter(tags=["Cards"])

async def check_category_exists(
        category_id: Optional[int],
        session: AsyncSession
):
    if category_id:
        stmt = select(Categories).where(Categories.id == category_id)
        result = await session.execute(stmt)
        if result.scalars().first() is None:
            raise HTTPException(status_code=400, detail="Category ID does not exist")


@router.get("", response_model=List[CardRead])
async def get_all_cards(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Cards).order_by(Cards.id)
    result = await session.scalars(stmt)
    cards = result.all()
    return cards


@router.post("", response_model=CardRead)
async def create_card(
    card_create: CardCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    await check_category_exists(card_create.category_id, session)

    card = Cards(**card_create.model_dump())
    session.add(card)

    await session.commit()
    await session.refresh(card)

    return card


@router.delete("/{card_id}", response_model=CardRead)
async def delete_card(
    card_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    stmt = select(Cards).where(Cards.id == card_id)
    result = await session.execute(stmt)
    card = result.scalars().first()

    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")

    await session.delete(card)
    await session.commit()

    return card


@router.get("/{card_id}", response_model=CardRead)
async def get_card(
    card_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    stmt = select(Cards).where(Cards.id == card_id)
    result = await session.execute(stmt)
    card = result.scalars().first()

    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")

    return card


@router.put("/{card_id}", response_model=CardRead)
async def update_card(
    card_id: int,
    card_update: CardUpdate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    stmt = select(Cards).where(Cards.id == card_id)
    result = await session.execute(stmt)
    card = result.scalars().first()

    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")

    await check_category_exists(card_update.category_id, session)

    for key, value in card_update.model_dump().items():
        setattr(card, key, value)
    session.add(card)

    await session.commit()
    await session.refresh(card)

    return card
