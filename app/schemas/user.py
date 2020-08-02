import re
from typing import Optional

from fastapi import HTTPException, status
from pydantic import BaseModel, validator

PHONE_REG_EXP = r"^7\d{10}$"


# Shared properties
class UserBase(BaseModel):
    email: Optional[str] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserRegistrationIn(BaseModel):
    phone: str

    @validator("phone")
    def phone_check(cls, value):
        if not re.match(PHONE_REG_EXP, value):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="phone_not_valid"
            )
        return value


class UserLogin(BaseModel):
    sms_code: str
    jwt_auth_token: str


class UserRefreshToken(BaseModel):
    refresh_token: str


class UserUpdate(BaseModel):
    name: str = None
    last_name: str = None
    blood_type: str = None
    birth_date: str = None
    weight: int = None
    height: int = None
