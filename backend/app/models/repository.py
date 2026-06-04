from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.base import Base

class Repository(Base):
    __tablename__ = "repositories"

    id: Mapped[int] = mapped_column(primary_key=True)

    github_repo_id: Mapped[int]

    name: Mapped[str] = mapped_column(
        String(255)
    )

    owner: Mapped[str] = mapped_column(
        String(255)
    )