from fastapi import APIRouter

from .users import router as users_router
from .cards import router as cards_router
from .categories import router as category_router

from core.config import settings

router = APIRouter(
    prefix=settings.api.prefix
)

router.include_router(
    router=users_router,
    prefix=settings.api.users
)

router.include_router(
    router=cards_router,
    prefix=settings.api.cards
)

router.include_router(
    router=category_router,
    prefix=settings.api.categories
)

__all__ = (
    "router"
)