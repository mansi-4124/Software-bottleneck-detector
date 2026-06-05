"""
Pull request model.
"""

from sqlalchemy import (
    Integer,
    String,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from app.db.base_class import Base


class PullRequest(Base):
    """
    Pull request metadata.
    """

    __tablename__ = "pull_requests"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    repository_id: Mapped[int] = mapped_column(
        ForeignKey(
            "repositories.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    github_pr_number: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(500),
        nullable=False
    )

    author: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    state: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    additions: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    deletions: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    changed_files: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False
    )

    merged_at: Mapped[DateTime | None] = mapped_column(
        DateTime,
        nullable=True
    )

    repository = relationship(
        "Repository",
        back_populates="pull_requests"
    )