"""
Commit model.
"""

from sqlalchemy import (
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime
)
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Commit(Base):
    """
    Git commit metadata.
    """

    __tablename__ = "commits"

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

    github_sha: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    message: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    author_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    author_email: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    commit_timestamp: Mapped[DateTime] = mapped_column(
        DateTime,
        nullable=False
    )

    repository = relationship(
        "Repository",
        back_populates="commits"
    )