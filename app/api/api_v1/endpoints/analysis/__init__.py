from fastapi import APIRouter

from .create import router as _create_router
from .get_by_category import router as _get_router
from .get_count import router as _get_count_router

analysis_router = APIRouter()
analysis_router.include_router(_create_router)
analysis_router.include_router(_get_count_router)
analysis_router.include_router(_get_router)
