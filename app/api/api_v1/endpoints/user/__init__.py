from fastapi import APIRouter

from .get import router as _get_router
from .update import router as _update_router

user_router = APIRouter()
user_router.include_router(_get_router)
user_router.include_router(_update_router)
