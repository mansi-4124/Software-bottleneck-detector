from datetime import datetime

from app.models.commit import Commit


def test_commit_model_creation():
    """
    Verify commit model creation.
    """

    commit = Commit(
        repository_id=1,
        github_sha="abc123",
        message="Initial commit",
        author_name="John Doe",
        author_email="john@example.com",
        commit_timestamp=datetime.utcnow()
    )

    assert commit.repository_id == 1
    assert commit.github_sha == "abc123"
    assert commit.message == "Initial commit"
    assert commit.author_name == "John Doe"