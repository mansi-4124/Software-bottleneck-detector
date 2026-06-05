"""
Tests for PullRequestRepository.
"""

from datetime import datetime

from app.repositories.pull_request_repository import (
    PullRequestRepository
)
from app.models.repository import Repository


def test_create_pull_request(
    db_session
):
    """
    Verify PR persistence.
    """

    repository = Repository(
        github_id=1,
        name="react",
        owner="facebook",
        full_name="facebook/react",
        default_branch="main",
        language="JavaScript",
        stars=100,
    )

    db_session.add(repository)
    db_session.commit()
    db_session.refresh(repository)

    repository_id = repository.id

    pr_repo = PullRequestRepository(
        db_session
    )

    pr = pr_repo.create(
        repository_id=repository_id,
        github_pr_number=123,
        title="Add auth",
        author="octocat",
        state="closed",
        additions=100,
        deletions=20,
        changed_files=5,
        created_at=datetime.utcnow(),
        merged_at=datetime.utcnow(),
    )

    assert pr.id is not None
    assert pr.github_pr_number == 123