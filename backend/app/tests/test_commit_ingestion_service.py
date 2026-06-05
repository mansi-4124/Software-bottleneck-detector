from unittest.mock import Mock

from app.services.commit_ingestion_service import (
    CommitIngestionService
)


def test_ingest_commits():

    github_client = Mock()
    github_service = Mock()
    commit_repository = Mock()

    github_client.fetch_commits.return_value = [
        {
            "sha": "abc123",
            "commit": {
                "message": "initial",
                "author": {
                    "name": "Mansi",
                    "email": "test@test.com",
                    "date": "2026-06-05T10:00:00Z"
                }
            }
        }
    ]

    github_service.parse_commit.return_value = {
        "github_sha": "abc123",
        "message": "initial",
        "author_name": "Mansi",
        "author_email": "test@test.com",
        "commit_timestamp":
            "2026-06-05T10:00:00Z"
    }

    commit_repository.get_by_sha.return_value = None

    service = CommitIngestionService(
        github_client=github_client,
        github_service=github_service,
        commit_repository=commit_repository,
    )

    service.ingest_commits(
        repository_id=1,
        owner="facebook",
        repo="react",
    )

    commit_repository.create.assert_called_once()