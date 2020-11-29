from fastapi import APIRouter

from .create import router as _create_router

analysis_router = APIRouter()
analysis_router.include_router(_create_router)
