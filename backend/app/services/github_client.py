"""
GitHub API client.
"""
import requests
import os

from app.core.config import settings


class GitHubClient:

    BASE_URL = "https://api.github.com"

    def __init__(self, token: str | None = None):
        self.token = token or os.getenv("GITHUB_TOKEN")

        if not self.token:
            raise ValueError("GITHUB_TOKEN is not configured")

    @classmethod
    def build_repo_url(
        cls,
        owner,
        repo
    ):

        return (
            f"{cls.BASE_URL}/repos/{owner}/{repo}"
        )
    
    @staticmethod
    def build_headers(
        token
    ):
        return {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json"
        }
    
    def fetch_repository(
        self,
        owner,
        repo
    ):
        response = requests.get(
            self.build_repo_url(owner, repo),
            headers=self.build_headers(
                settings.GITHUB_TOKEN
            ),
            timeout=30,
        )

        response.raise_for_status()

        return response.json()