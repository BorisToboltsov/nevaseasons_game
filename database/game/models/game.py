from sqlalchemy import Column, String, ForeignKey

from database.base.mixin.base_mixin import CreateMixin, SaveMixin, BaseMixin
from database.base.model.base import Base


class Game(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "game"
    __tableargs__ = {"comment": "Game"}

    name = Column(name="name", type_=String(30), comment="The name of the game")

    def __repr__(self):
        return f"{self.name}"
