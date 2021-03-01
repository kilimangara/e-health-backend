from fastapi import APIRouter

from .create import router as _create_router
from .get_by_user import router as _get_by_user_router

allergie_router = APIRouter()
allergie_router.include_router(_create_router)
allergie_router.include_router(_get_by_user_router)
