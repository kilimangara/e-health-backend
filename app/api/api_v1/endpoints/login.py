from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import (get_current_for_token_refresh,
                          get_current_user,
                          get_current_user_for_auth)
from app.core.security import create_jwt_auth_token, create_token
from app.db.base import SessionLocal
from app.db.models.user import STATUS_APPROVED, UserData
from app.schemas.user import UserLogin, UserRefreshToken, UserRegistrationIn
from app.utils.sms import send_sms

router = APIRouter()


def get_db():
    """Получение коннекта к БД."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", tags=["login"])
def register_or_authenticate(
    request_data: UserRegistrationIn, db: Session = Depends(get_db)
) -> Any:
    """Регистрация/запрос на авторизацию."""
    user = crud.user.get_by_phone(db, request_data.phone)
    if not user:
        user = crud.user.registrate(db, request_data)
    jwt_token, sms_code = create_jwt_auth_token(user)

    # send_sms(sms_code, request_data.phone)
    return {"result": {"jwt_token": jwt_token, "user_id": user.id}}


@router.post("/login/access-token", tags=["login"])
def login(request_data: UserLogin, db: Session = Depends(get_db)) -> Any:
    """Вход."""
    user, token_payload = get_current_user_for_auth(db, request_data.jwt_auth_token)
    if token_payload.sms_code != request_data.sms_code:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    user_update = {"status": STATUS_APPROVED}
    user = crud.user.update(db, db_obj=user, obj_in=user_update)

    return {
        "access_token": create_token(user.id),
        "refresh_token": create_token(user.id, "refresh_token", 3),
        "token_type": "bearer",
    }


@router.post("/refresh_token")
def refresh_token(request_data: UserRefreshToken, db: Session = Depends(get_db)) -> Any:
    """Обновление токена."""
    user, token_payload = get_current_for_token_refresh(db, request_data.refresh_token)

    return {
        "access_token": create_token(user.id),
        "refresh_token": create_token(user.id, "refresh_token", 3),
        "token_type": "bearer",
    }


@router.post("/test_route")
def test_route(current_user: UserData = Depends(get_current_user)):
    return {"result": {"user_id": current_user.id,}}
