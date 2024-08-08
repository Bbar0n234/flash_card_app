from fastapi import APIRouter

from .base_config import auth_backend, fastapi_users
from core.schemas import UserCreate, UserRead
from core.config import settings

main_router = APIRouter(
    prefix=settings.auth.prefix,
    tags=["Auth"]
)

main_router.include_router(
    fastapi_users.get_auth_router(auth_backend)
)

main_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate)
)

__all__ = (
    "main_router"
)