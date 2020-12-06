from fastapi import APIRouter

from .get import router as _get_router
from .update import router as _update_router
from .create_sub_user import router as _create_sub_user_router
from .change_user import router as _change_user_router
from .get_all_users import router as _get_all_users_router

user_router = APIRouter()
user_router.include_router(_get_router)
user_router.include_router(_update_router)
user_router.include_router(_create_sub_user_router)
user_router.include_router(_change_user_router)
user_router.include_router(_get_all_users_router)
