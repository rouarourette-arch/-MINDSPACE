
from sqlalchemy import Integer, String, Text, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import Base
from backend.models.enums import AnswerOption


class Question(Base):
    __tablename__ = "questions"

    question_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    quiz_id: Mapped[int] = mapped_column(
        ForeignKey("quizzes.quiz_id", ondelete="CASCADE"),
        nullable=False
    )
    question_text: Mapped[str] = mapped_column(
        Text, nullable=False
    )
    option_a: Mapped[str] = mapped_column(
        String(500), nullable=False
    )
    option_b: Mapped[str] = mapped_column(
        String(500), nullable=False
    )
    option_c: Mapped[str] = mapped_column(
        String(500), nullable=False
    )
    option_d: Mapped[str] = mapped_column(
        String(500), nullable=False
    )
    correct_answer: Mapped[AnswerOption] = mapped_column(
        Enum(
            AnswerOption,
            values_callable=lambda x: [e.value for e in x]
        ),
        nullable=False
    )
