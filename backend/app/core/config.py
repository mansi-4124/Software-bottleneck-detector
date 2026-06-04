"""
Application configuration.

Loads environment variables from .env
and exposes strongly-typed settings.
"""

from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    """
    Application settings container.
    """

    DATABASE_URL: str = os.getenv("DATABASE_URL")

    GITHUB_TOKEN: str = os.getenv("GITHUB_TOKEN")


settings = Settings()