from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, Categories
from core.schemas import CategoryCreate, CategoryRead, CategoryUpdate

from typing import List

router = APIRouter(tags=["Categories"])

@router.get("", response_model=List[CategoryRead])
async def get_all_categories(
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Categories).order_by(Categories.id)
    result = await session.scalars(stmt)
    categories = result.all()

    return categories


@router.get("/{id}", response_model=CategoryRead)
async def get_category_by_id(
    id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Categories).where(Categories.id == id)
    result = await session.execute(stmt)
    category = result.scalar_one_or_none()

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("", response_model=CategoryRead, status_code=201)
async def create_category(
    category_create: CategoryCreate,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    category = Categories(**category_create.dict())
    session.add(category)
    await session.commit()
    await session.refresh(category)
    
    return category


@router.delete("/{id}", response_model=CategoryRead)
async def delete_category(
    id: int,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Categories).where(Categories.id == id)
    result = await session.execute(stmt)
    category = result.scalar_one_or_none()

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    await session.delete(category)
    await session.commit()

    return category


@router.put("/{id}", response_model=CategoryRead)
async def update_category(
    id: int,
    category_update: CategoryUpdate,
    session: AsyncSession = Depends(db_helper.session_getter)
):
    stmt = select(Categories).where(Categories.id == id)
    result = await session.execute(stmt)
    category = result.scalar_one_or_none()

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    for key, value in category_update.model_dump(exclude_unset=True).items():
        setattr(category, key, value)

    await session.commit()
    await session.refresh(category)
    
    return category






