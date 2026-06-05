"""
GitHub API integration service.
"""

import requests

from app.core.config import settings


class GitHubService:
    """
    Service responsible for
    interacting with GitHub APIs.
    """

    BASE_URL = "https://api.github.com"

    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {settings.GITHUB_TOKEN}"
        }
    
    @staticmethod
    def parse_repository(data:dict)->dict:
        """
        Parse GitHub API response.
        """

        return {
            "github_id": data["id"],
            "name": data["name"],
            "owner": data["owner"]["login"],
            "full_name": data["full_name"],
            "description": data.get("description"),
            "default_branch": data["default_branch"],
            "language": data["language"],
            "stars": data["stargazers_count"]
        }