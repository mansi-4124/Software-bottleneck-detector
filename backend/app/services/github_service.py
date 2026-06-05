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

    @staticmethod
    def parse_commit(
        commit_data: dict,
    ):
        """
        Parse commit payload.
        """

        return {
            "github_sha": commit_data["sha"],
            "message": commit_data["commit"]["message"],
            "author_name":
                commit_data["commit"]["author"]["name"],
            "author_email":
                commit_data["commit"]["author"]["email"],
            "commit_timestamp":
                commit_data["commit"]["author"]["date"],
        }
    
    @staticmethod
    def parse_pull_request(
        data: dict
    ):
        """
        Parse GitHub PR response.
        """

        return {
            "github_pr_number": data["number"],
            "title": data["title"],
            "author": data["user"]["login"],
            "state": data["state"],
            "additions": data["additions"],
            "deletions": data["deletions"],
            "changed_files": data["changed_files"],
            "created_at": data["created_at"],
            "merged_at": data["merged_at"],
        }