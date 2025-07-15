# config.py (for Pydantic v2)
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = {
        "env_file": ".env",
        "extra": "ignore",
    }


settings = Settings()
