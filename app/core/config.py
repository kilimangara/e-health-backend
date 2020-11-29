import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import (AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn,
                      validator)


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30
    SMS_TOKEN_EXPIRE_MINUTES: int = 15
    SERVER_NAME: str
    SERVER_HOST: AnyHttpUrl
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "E-HEALTH"
    SENTRY_DSN: Optional[HttpUrl] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            return None
        return v

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Union[PostgresDsn, str] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def db_url(self):
        return f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}/{self.POSTGRES_DB}"

    # SMS CONFIG
    SMS_SENDER_ENABLED: bool = False
    SMS_SENDER_LOGIN: str = "kilimangara"
    SMS_SENDER_PASSWORD: str = "131196"

    # AMAZON_S3
    AMAZON_SERVICE_NAME: str = "s3"
    AMAZON_REGION_NAME: str = "eu-north-1"
    AMAZON_ACCESS_KEY_ID: str = "AKIAV44LYBIXFGPPXI6O"
    AMAZON_SECRET_ACCESS_KEY: str = "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"
    AMAZON_BUCKET_NAME: str = "emma-e-health-test"


settings = Settings()
