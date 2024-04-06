from sqlalchemy import Column, ForeignKey, String

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class Game(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "game"
    __tableargs__ = {"comment": "Game"}

    name = Column(name="name", type_=String(30), comment="The name of the game")

    def __repr__(self):
        return f"{self.name}"
