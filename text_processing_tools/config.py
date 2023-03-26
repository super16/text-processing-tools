from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_engine: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings():
    return Settings()
