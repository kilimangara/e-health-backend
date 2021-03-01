from fastapi import APIRouter

from .approve_avatar import router as _approve_avatar_router
from .create_list import router as _create_list_router

images_router = APIRouter()
images_router.include_router(_create_list_router)
images_router.include_router(_approve_avatar_router)
