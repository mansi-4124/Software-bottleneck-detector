"""
Repository access layer
for pull requests.
"""

from sqlalchemy.orm import Session

from app.models.pull_request import (
    PullRequest
)


class PullRequestRepository:
    """
    Database operations
    for pull requests.
    """

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(
        self,
        **kwargs
    ) -> PullRequest:

        pull_request = PullRequest(
            **kwargs
        )

        self.db.add(
            pull_request
        )

        self.db.commit()

        self.db.refresh(
            pull_request
        )

        return pull_request

    def get_by_pr_number(
        self,
        github_pr_number: int
    ):
        return (
            self.db.query(
                PullRequest
            )
            .filter(
                PullRequest.github_pr_number
                == github_pr_number
            )
            .first()
        )