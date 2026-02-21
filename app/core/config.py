import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_NAME: str = "SAIS"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./sais.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change-me")
    STORAGE_DIR: str = os.getenv("STORAGE_DIR", "./storage")


settings = Settings()
