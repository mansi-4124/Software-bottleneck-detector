from sqlalchemy import String
from sqlalchemy import BigInteger
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base_class import Base


class Repository(Base):
    """
    Stores GitHub repository metadata.
    """

    __tablename__ = "repositories"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    github_id: Mapped[int] = mapped_column(
        BigInteger,
        unique=True,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str] = mapped_column(
        String(255),
        nullable=True
    )

    full_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    owner: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    default_branch: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    language: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True
    )

    stars: Mapped[int] = mapped_column(
        Integer,
        default=0
    )

    commits = relationship(
        "Commit",
        backref="repository",
        cascade="all, delete-orphan"
    )