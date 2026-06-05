"""
Repository ingestion workflow.

Coordinates:
GitHub API
    ↓
Parse
    ↓
Persist
"""

from app.services.github_client import GitHubClient
from app.services.github_service import GitHubService
from app.repositories.repository_repository import (
    RepositoryRepository
)


class RepositoryIngestionService:
    """
    Repository ingestion workflow.
    """

    def __init__(
        self,
        github_client: GitHubClient,
        github_service: GitHubService,
        repository_repo: RepositoryRepository,
    ):
        self.github_client = github_client
        self.github_service = github_service
        self.repository_repo = repository_repo

    def ingest_repository(
        self,
        owner: str,
        repo: str,
    ):
        """
        Fetch repository,
        parse response,
        save into database.
        """

        raw_repository = self.github_client.fetch_repository(
            owner=owner,
            repo=repo
        )

        parsed_repository = (
            self.github_service.parse_repository(
                raw_repository
            )
        )

        existing_repository = (
            self.repository_repo.get_by_github_id(
                parsed_repository["github_id"]
            )
        )

        if existing_repository:
            return existing_repository

        saved_repository = (
            self.repository_repo.create(
                **parsed_repository
            )
        )

        return saved_repository