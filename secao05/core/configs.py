from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://guilherme:etabeta@localhost:5432/fastapi"

    class Config:
        case_sensitive = True


settings: Settings = Settings()