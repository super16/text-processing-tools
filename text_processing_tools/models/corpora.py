from sqlalchemy import INTEGER, TEXT
from sqlalchemy.orm import Mapped, mapped_column

from text_processing_tools.models import Base


class Corpus(Base):
    __tablename__ = "corpora"

    id: Mapped[int] = mapped_column(
        INTEGER(),
        autoincrement=True,
        index=True,
        primary_key=True,
        unique=True,
    )
    title: Mapped[str] = mapped_column(
        TEXT,
        nullable=False
    )
