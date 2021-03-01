from fastapi import APIRouter

from .access_token import router as _access_router
from .login import router as _login_router
from .refresh_token import router as _refresh_router

login_router = APIRouter()
login_router.include_router(_login_router)
login_router.include_router(_access_router)
login_router.include_router(_refresh_router)
