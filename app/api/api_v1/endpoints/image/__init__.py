from fastapi import APIRouter

from .create_list import router as _create_list_router

images_router = APIRouter()
images_router.include_router(_create_list_router)
