from fastapi import APIRouter

from app.api.api_v1.endpoints.allergie import allergie_router
from app.api.api_v1.endpoints.image import images_router
from app.api.api_v1.endpoints.login import login_router
from app.api.api_v1.endpoints.user import user_router
from app.api.api_v1.endpoints.analysis import analysis_router

api_router = APIRouter()
api_router.include_router(login_router, tags=["login"], prefix="/login")
api_router.include_router(user_router, tags=["user"], prefix="/user")
api_router.include_router(allergie_router, tags=["allergia"], prefix="/allergia")
api_router.include_router(images_router, tags=["images"], prefix="/images")
api_router.include_router(analysis_router, tags=["analysis"], prefix="/analysis")
