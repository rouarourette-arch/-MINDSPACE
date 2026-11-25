
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import Base


class Quiz(Base):
    __tablename__ = "quizzes"

    quiz_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    title: Mapped[str] = mapped_column(
        String(200), nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )
    category: Mapped[str] = mapped_column(
        String(100), nullable=False
    )
