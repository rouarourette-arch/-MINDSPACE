
from sqlalchemy import (
    Integer, String, Text, DateTime, ForeignKey, Enum
)
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from backend.database.base import Base
from backend.models.enums import Priority, TaskStatus


class Task(Base):
    __tablename__ = "tasks"

    task_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )
    category_id: Mapped[int | None] = mapped_column(
        ForeignKey("categories.category_id", ondelete="SET NULL"),
        nullable=True
    )
    title: Mapped[str] = mapped_column(
        String(200), nullable=False
    )
    description: Mapped[str | None] = mapped_column(
        Text, nullable=True
    )
    priority: Mapped[Priority] = mapped_column(
        Enum(Priority, values_callable=lambda x: [e.value for e in x]),
        default=Priority.MEDIUM,
        nullable=False
    )
    deadline: Mapped[DateTime | None] = mapped_column(
        DateTime, nullable=True
    )
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus, values_callable=lambda x: [e.value for e in x]),
        default=TaskStatus.PENDING,
        nullable=False
    )
    estimated_minutes: Mapped[int | None] = mapped_column(
        Integer, nullable=True
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now(),
        onupdate=func.now()
    )
