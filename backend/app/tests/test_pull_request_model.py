"""
Tests for PullRequest model.
"""

from datetime import datetime

from app.models.pull_request import PullRequest


def test_pull_request_model_creation():
    """
    Verify pull request model fields.
    """

    pr = PullRequest(
        repository_id=1,
        github_pr_number=123,
        title="Add authentication",
        author="octocat",
        state="closed",
        additions=100,
        deletions=20,
        changed_files=5,
        created_at=datetime.utcnow(),
        merged_at=datetime.utcnow(),
    )

    assert pr.github_pr_number == 123
    assert pr.author == "octocat"
    assert pr.additions == 100