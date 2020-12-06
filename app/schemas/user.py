import re

from fastapi import HTTPException, status
from pydantic import BaseModel, validator

PHONE_REG_EXP = r"^7\d{10}$"


class UserCreateModel(BaseModel):
    """Схема запроса."""

    phone: str

    @validator("phone")
    def phone_check(cls, value):
        """Валидация телефона."""
        if not re.match(PHONE_REG_EXP, value):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="phone_not_valid"
            )
        return value


class UserUpdateModel(BaseModel):
    """Схема обновления пользователя."""

    name: str = None
    last_name: str = None
    blood_type: str = None
    birth_date: str = None
    weight: int = None
    height: int = None


class ChangeUserModel(BaseModel):
    """Схема изменения пользователя."""
    id: int
