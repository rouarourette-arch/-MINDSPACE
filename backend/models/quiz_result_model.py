
from sqlalchemy import Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from backend.database.base import Base


class QuizResult(Base):
    __tablename__ = "quiz_results"

    result_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )
    quiz_id: Mapped[int] = mapped_column(
        ForeignKey("quizzes.quiz_id", ondelete="CASCADE"),
        nullable=False
    )
    score: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    total_questions: Mapped[int] = mapped_column(
        Integer, nullable=False
    )
    completed_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now()
    )
