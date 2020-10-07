import random
from datetime import datetime, timedelta

from jose import jwt

from app.core.config import settings
from app.db.models.user import Users

ALGORITHM = "HS256"


def create_token(
    user_id: int, type: str = "access_token", time_multiplier: int = 1
) -> str:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES * time_multiplier
    )
    to_encode = {"exp": expire, "user_id": str(user_id), "type": type}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_jwt_auth_token(user: Users) -> (str, str):
    """Создание токена для последующей авторизации."""
    # сделать в зависимости от окружения
    # sms_code = create_sms_code()
    sms_code = "123456"
    expire = datetime.utcnow() + timedelta(minutes=settings.SMS_TOKEN_EXPIRE_MINUTES)
    data = {
        "exp": expire,
        "user_id": user.id,
        "sms_code": sms_code,
        "phone": user.phone,
        "type": "auth_token",
    }
    jwt_token = jwt.encode(data, settings.SECRET_KEY, algorithm=ALGORITHM)

    return jwt_token, sms_code


def create_sms_code() -> str:
    """Создание смс кода."""
    return "{:0=6}".format((random.randint(0, 999999)))
