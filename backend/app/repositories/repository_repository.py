"""
Repository persistence operations.
"""

from sqlalchemy.orm import Session

from app.models.repository import Repository


class RepositoryRepository:
    """
    Handles repository persistence.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        github_id: int,
        name: str,
        owner: str,
        full_name: str,
        description: str | None,
        default_branch: str,
        language: str | None,
        stars: int,
    ) -> Repository:
        """
        Persist repository.
        """

        repository = Repository(
            github_id=github_id,
            name=name,
            owner=owner,
            full_name=full_name,
            description=description,
            default_branch=default_branch,
            language=language,
            stars=stars,
        )

        self.db.add(repository)
        self.db.commit()
        self.db.refresh(repository)

        return repository

    def get_by_github_id(
        self,
        github_id: int
    ) -> Repository | None:
        """
        Find repository by GitHub ID.
        """

        return (
            self.db.query(Repository)
            .filter(
                Repository.github_id == github_id
            )
            .first()
        )

    def get_by_full_name(
        self,
        full_name: str
    ) -> Repository | None:
        """
        Find repository by owner/repo.
        """

        return (
            self.db.query(Repository)
            .filter(
                Repository.full_name == full_name
            )
            .first()
        )