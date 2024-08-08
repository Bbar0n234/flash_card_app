from fastapi import APIRouter

from .users import router as users_router
from .cards import router as cards_router
from .categories import router as category_router
from .user_card import router as user_card_router
from .answers import router as answers_router

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

router.include_router(
    router=user_card_router,
    prefix=settings.api.user_card
)

router.include_router(
    router=answers_router,
    prefix=settings.api.answers
)

__all__ = (
    "router"
)