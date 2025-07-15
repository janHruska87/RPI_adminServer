from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./test.db"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
