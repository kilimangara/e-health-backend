from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_db, get_current_user_is_approved
from app.core.security import create_token
from app.db.models.user import UsersDBModel

router = APIRouter()


@router.post("/createSubUser")
async def register_or_authenticate(
    current_user: UsersDBModel = Depends(get_current_user_is_approved),
    db: Session = Depends(get_db),
) -> Any:
    """Регистрация/запрос на авторизацию."""
    if current_user.parent_user_id is not None:
        raise HTTPException(status.HTTP_403_FORBIDDEN, "You should create user from main account")
    user_id = await crud.user.create_sub_user(db, current_user.id)
    jwt_token = create_token(user_id)

    return {"result": {"jwt_token": jwt_token, "new_user_id": user_id}}
