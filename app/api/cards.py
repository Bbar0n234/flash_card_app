from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Cards
from core.schemas import CardRead, CardCreate, CardUpdate
from typing import List

router = APIRouter(tags=["Cards"])

@router.get("", response_model=List[CardRead])
async def get_all_cards(
        session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Cards).order_by(Cards.id)
    result = await session.scalars(stmt)
    cards = result.all()
    return cards

@router.post("", response_model=CardRead, status_code=status.HTTP_201_CREATED)
async def create_card(
    card_create: CardCreate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    card = Cards(**card_create.model_dump())
    session.add(card)
    await session.commit()
    await session.refresh(card)
    return card


@router.get("/{card_id}", response_model=CardRead)
async def get_card(card_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    stmt = select(Cards).where(Cards.id == card_id)
    result = await session.scalars(stmt)
    card = result.one_or_none()
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return card


@router.delete("/{card_id}", response_model=CardRead)
async def delete_card(card_id: int, session: AsyncSession = Depends(db_helper.session_getter)):
    stmt = select(Cards).where(Cards.id == card_id)
    result = await session.scalars(stmt)
    card = result.one_or_none()
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    await session.delete(card)
    await session.commit()
    return card


@router.put("/{card_id}", response_model=CardRead)
async def update_card(
    card_id: int,
    card_update: CardUpdate,
    session: AsyncSession = Depends(db_helper.session_getter),
):
    stmt = select(Cards).where(Cards.id == card_id)
    result = await session.scalars(stmt)
    card = result.one_or_none()
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    for key, value in card_update.model_dump(exclude_unset=True).items():
        setattr(card, key, value)
    session.add(card)
    await session.commit()
    await session.refresh(card)
    return card
