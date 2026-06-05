from unittest.mock import Mock

from app.services.repository_ingestion_service import (
    RepositoryIngestionService
)


def test_ingest_repository():
    """
    Verify repository can be fetched,
    parsed and persisted.
    """

    github_client = Mock()
    github_service = Mock()
    repository_repo = Mock()

    github_client.fetch_repository.return_value = {
        "id": 123,
        "name": "react"
    }

    github_service.parse_repository.return_value = {
        "github_id": 123,
        "name": "react",
        "owner": "facebook",
        "full_name": "facebook/react",
        "description": "React library",
        "default_branch": "main",
        "language": "JavaScript",
        "stars": 100
    }

    repository_repo.get_by_github_id.return_value = None

    repository_repo.create.return_value = {
        "id": 1
    }

    service = RepositoryIngestionService(
        github_client=github_client,
        github_service=github_service,
        repository_repo=repository_repo
    )

    result = service.ingest_repository(
        owner="facebook",
        repo="react"
    )

    github_client.fetch_repository.assert_called_once_with(
        owner="facebook",
        repo="react"
    )

    github_service.parse_repository.assert_called_once()

    repository_repo.create.assert_called_once()

    assert result == {"id": 1}

def test_ingest_existing_repository():
    github_client = Mock()
    github_service = Mock()
    repository_repo = Mock()

    github_client.fetch_repository.return_value = {
        "id": 123
    }

    github_service.parse_repository.return_value = {
        "github_id": 123
    }

    repository_repo.get_by_github_id.return_value = {
        "id": 5
    }

    service = RepositoryIngestionService(
        github_client,
        github_service,
        repository_repo
    )

    result = service.ingest_repository(
        owner="facebook",
        repo="react"
    )

    repository_repo.create.assert_not_called()

    assert result["id"] == 5