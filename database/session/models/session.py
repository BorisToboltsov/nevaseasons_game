from sqlalchemy import Column, Integer, ForeignKey, Boolean

from database.base.mixin.base_mixin import CreateMixin, SaveMixin, BaseMixin
from database.base.model.base import Base


class Session(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "group"
    __tableargs__ = {"comment": "Group"}

    number_participants = Column(name="number_participants", type_=Integer, comment="Number Participants")
    game_id = Column(
        ForeignKey("game.id", ondelete="NO ACTION"),
        nullable=False,
    )
    user_id = Column(
        ForeignKey("user.id", ondelete="NO ACTION"),
        nullable=False,
    )
    is_finished = Column(name="is_finished", type_=Boolean, comment="Game is finished")

    def __repr__(self):
        return f"{self.game_id}"
