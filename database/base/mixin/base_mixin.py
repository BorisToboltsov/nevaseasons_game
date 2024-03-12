from sqlalchemy import JSON, Boolean, Column, DateTime, Integer
from sqlalchemy.sql import func

from database.connect_db import engine, get_session

session = get_session(engine)


class BaseMixin:
    id = Column(
        name="id",
        type_=Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
        unique=True,
    )
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        comment="Дата и время создания",
    )
    updated_at = Column(
        DateTime(timezone=True), onupdate=func.now(), comment="Дата и время изменения"
    )
    is_active = Column(Boolean, default=True)
    is_delete = Column(Boolean, default=False)
    sub_data = Column(JSON, nullable=True)


class CreateMixin:
    @classmethod
    def create(cls, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        return obj


class SaveMixin:
    @classmethod
    def save(cls, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        return obj
