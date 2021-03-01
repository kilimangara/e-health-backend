from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_db
from app.core.security import create_jwt_auth_token
from app.schemas.user import UserCreateModel
from app.utils.sms import send_sms

router = APIRouter()


@router.post("/login")
async def register_or_authenticate(
    request_data: UserCreateModel, db: Session = Depends(get_db)
) -> Any:
    """Регистрация/запрос на авторизацию."""
    user = await crud.user.get_by_phone(db, request_data.phone)
    if not user:
        user = await crud.user.registrate(db, request_data)
    jwt_token, sms_code = create_jwt_auth_token(user)

    send_sms(sms_code, request_data.phone)
    return {"result": {"jwt_token": jwt_token, "user_id": user.id}}
