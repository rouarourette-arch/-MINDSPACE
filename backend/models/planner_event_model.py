
from sqlalchemy import Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from backend.database.base import Base


class PlannerEvent(Base):
    __tablename__ = "planner_events"

    event_id: Mapped[int] = mapped_column(
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
    title: Mapped[str] = mapped_column(
        String(200), nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )
    start_datetime: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False
    )
    end_datetime: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now()
    )
