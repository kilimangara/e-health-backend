from datetime import datetime
from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import crud, schemas
from app.core import security
from app.core.config import settings
from app.db.base import SessionLocal
from app.db.models.user import UsersDBModel

reusable_oauth2 = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login/access-token"
)


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(reusable_oauth2)
) -> UsersDBModel:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.AccessToken(**payload)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Try to refresh token"
        )
    except (jwt.JWTError, ValidationError) as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Could not validate credentials, {str(e)}",
        )
    if token_data.type != "access_token":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not valid type of token"
        )

    user = await crud.user.get(db, id=token_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def get_current_user_for_auth(
    db: Session, token: str
) -> (UsersDBModel, schemas.AuthorizationToken):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.AuthorizationToken(**payload)
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Token expired"
        )
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    user = await crud.user.get_by_phone(db, token_data.phone)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    else:
        return user, token_data


async def get_current_for_token_refresh(
    db: Session, token: str
) -> (UsersDBModel, schemas.RefreshToken):
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[security.ALGORITHM]
        )
        token_data = schemas.RefreshToken(**payload)
    except (jwt.JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    if token_data.type != "refresh_token":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not valid type of token"
        )
    if datetime.fromtimestamp(token_data.exp) < datetime.utcnow():
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )

    user = await crud.user.get(db, id=token_data.user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    else:
        return user, token_data
