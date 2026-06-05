"""
Commit repository layer.
"""

from sqlalchemy.orm import Session

from app.models.commit import Commit


class CommitRepository:
    """
    Database operations
    for Commit model.
    """

    def __init__(
        self,
        db: Session
    ):
        self.db = db

    def create(
        self,
        repository_id: int,
        github_sha: str,
        message: str,
        author_name: str,
        author_email: str,
        commit_timestamp,
    ) -> Commit:
        """
        Persist commit.
        """

        commit = Commit(
            repository_id=repository_id,
            github_sha=github_sha,
            message=message,
            author_name=author_name,
            author_email=author_email,
            commit_timestamp=commit_timestamp,
        )

        self.db.add(commit)
        self.db.commit()
        self.db.refresh(commit)

        return commit

    def get_by_sha(
        self,
        github_sha: str,
    ):
        """
        Lookup commit by SHA.
        """

        return (
            self.db.query(Commit)
            .filter(
                Commit.github_sha == github_sha
            )
            .first()
        )