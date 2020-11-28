from fastapi import APIRouter

from app.api.api_v1.endpoints import login
from app.api.api_v1.endpoints import user
from app.api.api_v1.endpoints import allergies
from app.api.api_v1.endpoints import images

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(user.router, tags=["user"], prefix='/user')
api_router.include_router(allergies.router, tags=["allergia"], prefix='/allergia')
api_router.include_router(images.router, tags=['images'], prefix='/images')
