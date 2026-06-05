from datetime import datetime

from app.repositories.commit_repository import (
    CommitRepository
)


def test_create_commit(
    db_session
):
    repo = CommitRepository(db_session)

    commit = repo.create(
        repository_id=1,
        github_sha="abc123",
        message="Initial commit",
        author_name="Mansi",
        author_email="mansi@test.com",
        commit_timestamp=datetime.utcnow(),
    )

    assert commit.id is not None
    assert commit.github_sha == "abc123"


def test_get_by_sha(
    db_session
):
    repo = CommitRepository(db_session)

    repo.create(
        repository_id=1,
        github_sha="xyz789",
        message="Test",
        author_name="Mansi",
        author_email="mansi@test.com",
        commit_timestamp=datetime.utcnow(),
    )

    commit = repo.get_by_sha(
        "xyz789"
    )

    assert commit is not None
    assert commit.github_sha == "xyz789"