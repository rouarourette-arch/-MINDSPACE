
from sqlalchemy import Integer, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import Base


class FocusSession(Base):
    __tablename__ = "focus_sessions"

    session_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )
    task_id: Mapped[int | None] = mapped_column(
        ForeignKey("tasks.task_id", ondelete="SET NULL"),
        nullable=True
    )
    start_datetime: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False
    )
    end_datetime: Mapped[DateTime | None] = mapped_column(
        DateTime, nullable=True
    )
    duration_minutes: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False
    )
    completed: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
