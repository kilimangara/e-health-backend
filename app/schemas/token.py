import datetime
from typing import Optional

from pydantic import BaseModel


class AuthorizationToken(BaseModel):
    user_id: int
    phone: str
    sms_code: str


class TokenPayload(BaseModel):
    user_id: Optional[int] = None
    exp: Optional[str] = None
