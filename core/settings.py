from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    secret_key: str = Field(..., env = "SECRET_KEY")
    algorithm : str = Field(..., env = "ALGORITHM")
    database_url : str = Field(..., env = "DATABASE_URL")
    access_token_expire_minutes : int = Field(..., env = "ACCESS_TOKEN_EXPIRE_MINUTES")

    class Config:
        env_file = ".env"


settings = Settings()