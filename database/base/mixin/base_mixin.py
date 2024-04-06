from sqlalchemy import JSON, Boolean, Column, DateTime, Integer
from sqlalchemy.sql import func

from config.database import load_database

database_config = load_database()
sm = database_config.get_sessionmaker


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
    def create(cls, session, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        return obj


class SaveMixin:
    @classmethod
    def save(cls, session, **kwargs):
        obj = cls(**kwargs)
        session.add(obj)
        session.commit()
        return obj
