
from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from backend.database.base import Base


class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    username: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False
    )
    password_hash: Mapped[str] = mapped_column(
        String(255), nullable=False
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, server_default=func.now()
    )
