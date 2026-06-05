"""
Tests for PullRequestRepository.
"""

from datetime import datetime

from app.repositories.pull_request_repository import (
    PullRequestRepository
)


def test_create_pull_request(
    db_session
):
    """
    Verify PR persistence.
    """

    repository = db_session.execute(
        """
        INSERT INTO repositories
        (
            github_id,
            name,
            owner,
            full_name,
            default_branch,
            language,
            stars
        )
        VALUES
        (
            1,
            'react',
            'facebook',
            'facebook/react',
            'main',
            'JavaScript',
            100
        )
        RETURNING id
        """
    )

    repository_id = repository.scalar()

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