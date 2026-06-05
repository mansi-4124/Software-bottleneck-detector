"""
Commit ingestion workflow.
"""

from datetime import datetime

from app.services.github_client import GitHubClient
from app.services.github_service import GitHubService
from app.repositories.commit_repository import CommitRepository


class CommitIngestionService:
    """
    Fetch, parse and persist commits.
    """

    def __init__(
        self,
        github_client: GitHubClient,
        github_service: GitHubService,
        commit_repository: CommitRepository,
    ):
        self.github_client = github_client
        self.github_service = github_service
        self.commit_repository = commit_repository

    def ingest_commits(
        self,
        repository_id: int,
        owner: str,
        repo: str,
    ):
        """
        Fetch and store commits.
        """

        commits = self.github_client.fetch_commits(
            owner=owner,
            repo=repo,
        )

        saved_commits = []

        for commit in commits:

            parsed_commit = (
                self.github_service.parse_commit(
                    commit
                )
            )

            existing_commit = (
                self.commit_repository.get_by_sha(
                    parsed_commit["github_sha"]
                )
            )

            if existing_commit:
                continue

            parsed_commit["repository_id"] = (
                repository_id
            )

            parsed_commit["commit_timestamp"] = (
                datetime.fromisoformat(
                    parsed_commit[
                        "commit_timestamp"
                    ].replace(
                        "Z",
                        "+00:00"
                    )
                )
            )

            saved_commit = (
                self.commit_repository.create(
                    **parsed_commit
                )
            )

            saved_commits.append(
                saved_commit
            )

        return saved_commits