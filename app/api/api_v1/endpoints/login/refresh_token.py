from typing import Any

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.api.deps import get_current_for_token_refresh, get_db
from app.core.security import create_token

router = APIRouter()


class UserRefreshToken(BaseModel):
    """Схема запроса на обновление токена."""

    refresh_token: str


@router.post("/refreshToken")
async def refresh_token(
    request_data: UserRefreshToken, db: Session = Depends(get_db)
) -> Any:
    """Обновление токена."""
    user, token_payload = await get_current_for_token_refresh(
        db, request_data.refresh_token
    )

    return {
        "access_token": create_token(user.id),
        "refresh_token": create_token(user.id, "refresh_token", 3),
        "token_type": "bearer",
    }
