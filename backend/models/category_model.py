
from sqlalchemy import Integer, String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.base import Base


class Category(Base):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.user_id", ondelete="CASCADE"),
        nullable=False
    )
    name: Mapped[str] = mapped_column(
        String(100), nullable=False
    )

    __table_args__ = (
        UniqueConstraint("user_id", "name"),
    )
