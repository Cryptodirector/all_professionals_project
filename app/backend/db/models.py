from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, Integer
from app.backend.db.config import Base
from sqlalchemy import TIMESTAMP
import datetime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import ARRAY


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    surname: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False)
    qualification: Mapped[int] = mapped_column(nullable=True)  # квалификация, классность
    telegram_id: Mapped[str] = mapped_column(nullable=True)
    ready_business_trip: Mapped[bool] = mapped_column(nullable=False)
    experience: Mapped[int] = mapped_column(nullable=False)  # опыт работы

    id_prof: Mapped[list[int]] = mapped_column(
        ARRAY(Integer()),
        nullable=False
    )
    id_city: Mapped[int] = mapped_column(
        ForeignKey('city.id'),
        nullable=False
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )


class Profession(Base):
    __tablename__ = 'profession'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)


class NumberExecutor(Base):
    __tablename__ = 'number'
    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(nullable=False, unique=True)
    id_users: Mapped[int] = mapped_column(
        ForeignKey('users.id'),
        nullable=False
    )


class City(Base):
    __tablename__ = 'city'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)