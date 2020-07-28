import random
from datetime import datetime, timedelta

from jose import jwt

from app.core.config import settings
from app.db.models.user import UserData

ALGORITHM = "HS256"


def create_access_token(user_id: int, expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode = {"exp": expire, "user_id": str(user_id)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_jwt_auth_token(user: UserData) -> (str, str):
    """Создание токена для последующей авторизации."""
    sms_code = create_sms_code()
    sms_code = "123456"
    data = {"user_id": user.id, "sms_code": sms_code, "phone": user.phone}
    jwt_token = jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)

    return jwt_token, sms_code


def create_sms_code() -> str:
    """Создание смс кода."""
    return "{:0=6}".format((random.randint(0, 999999)))
