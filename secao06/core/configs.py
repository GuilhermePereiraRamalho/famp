from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.decl_api import DeclarativeMeta
from typing import ClassVar


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://guilherme:etabeta@localhost:5432/fastapi"
    DBBaseModel: ClassVar[DeclarativeMeta] = declarative_base()
    JWT_SECRET: str = "Uiydix9ZpAb7vyjYrnguVWHlIoJ8R6rZq7FoiDgwSiA"
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7

    class Config:
        case_sensitive = True


settings = Settings()