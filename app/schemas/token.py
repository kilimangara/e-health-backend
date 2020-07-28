import datetime
from typing import Optional

from pydantic import BaseModel


class AuthorizationToken(BaseModel):
    user_id: int
    phone: str
    sms_code: str
    type: str


class AccessToken(BaseModel):
    user_id: Optional[int] = None
    exp: Optional[float] = None
    type: str


class RefreshToken(BaseModel):
    user_id: Optional[int] = None
    exp: Optional[float] = None
    type: str
