from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user, get_current_user_for_auth
from app.core.security import create_access_token, create_jwt_auth_token
from app.db.base import SessionLocal
from app.db.models.user import STATUS_APPROVED, UserData
from app.schemas.user import UserLogin, UserRegistrationIn

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

    # send_sms(phone, sms_code)
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
        "access_token": create_access_token(user.id),
        "token_type": "bearer",
    }


@router.post("/test_route")
def test_route(current_user: UserData = Depends(get_current_user)):
    return {"result": {"user_id": current_user.id,}}
