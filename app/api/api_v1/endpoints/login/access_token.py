from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import crud
from app.api.deps import get_current_user_for_auth, get_db
from app.core.security import create_token
from app.db.models.user import STATUS_APPROVED

router = APIRouter()


class UserLogin(BaseModel):
    sms_code: str
    jwt_auth_token: str


@router.post("/accessToken", tags=["login"])
async def login(request_data: UserLogin, db: Session = Depends(get_db)) -> Any:
    """Авторизация."""
    user, token_payload = await get_current_user_for_auth(
        db, request_data.jwt_auth_token
    )
    if token_payload.sms_code != request_data.sms_code:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    return {
        "access_token": create_token(user.id),
        "refresh_token": create_token(user.id, "refresh_token", 3),
        "token_type": "bearer",
    }
