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

    def get_repository(
        self,
        owner: str,
        repo: str
    ) -> dict:
        """
        Fetch repository details
        from GitHub.
        """

        url = (
            f"{self.BASE_URL}/repos/"
            f"{owner}/{repo}"
        )

        response = requests.get(
            url,
            headers=self.headers,
            timeout=30
        )

        response.raise_for_status()

        data = response.json()

        return {
            "id": data["id"],
            "name": data["name"],
            "owner": data["owner"]["login"],
            "url": data["html_url"]
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
            "default_branch": data["default_branch"],
            "language": data["language"],
            "stars": data["stargazers_count"]
        }