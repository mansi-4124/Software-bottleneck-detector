"""
Tests for RepositoryRepository.
"""

from app.models.repository import Repository
from app.repositories.repository_repository import RepositoryRepository


def test_create_repository(db_session):
    """
    Verify repository can be persisted.
    """

    repository_repo = RepositoryRepository(db_session)

    repository = repository_repo.create(
        github_id=123456,
        name="react",
        owner="facebook",
        full_name="facebook/react",
        description="React library",
        default_branch="main",
        language="JavaScript",
        stars=100
    )

    assert repository.id is not None
    assert repository.github_id == 123456
    assert repository.full_name == "facebook/react"


def test_get_repository_by_github_id(db_session):
    """
    Verify repository lookup by GitHub ID.
    """

    repository_repo = RepositoryRepository(db_session)

    repository_repo.create(
        github_id=999,
        name="repo",
        owner="facebook",
        full_name="owner/repo",
        description="test repo",
        default_branch="main",
        language="Python",
        stars=10
    )

    repository = repository_repo.get_by_github_id(999)

    assert repository is not None
    assert repository.github_id == 999


def test_get_repository_by_full_name(db_session):
    """
    Verify repository lookup by full name.
    """

    repository_repo = RepositoryRepository(db_session)

    repository_repo.create(
        github_id=888,
        name="repo",
        owner="facebook",
        full_name="facebook/react",
        description="test repo",
        default_branch="main",
        language="Python",
        stars=10
    )

    repository = repository_repo.get_by_full_name(
        "facebook/react"
    )

    assert repository is not None
    assert repository.full_name == "facebook/react"