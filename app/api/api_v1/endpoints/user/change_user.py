from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_db, get_current_user
from app.core.security import create_token
from app.db.models.user import UsersDBModel
from app.schemas.user import ChangeUserModel

router = APIRouter()


@router.post("/changeUser")
async def register_or_authenticate(
    request_data: ChangeUserModel,
    current_user: UsersDBModel = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> Any:
    """Регистрация/запрос на авторизацию."""
    user = await crud.user.get(db, request_data.id)
    if user.parent_user_id == current_user.id or current_user.parent_user_id == user.id:
        return {"result": {"jwt_token": create_token(user.id), "user_id": user.id}}

    raise HTTPException(status.HTTP_403_FORBIDDEN, "Bad user id.")

