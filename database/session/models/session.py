from sqlalchemy import Column, Integer, ForeignKey, Boolean, String

from database.base.mixin.base_mixin import CreateMixin, SaveMixin, BaseMixin
from database.base.model.base import Base


class Session(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "session"
    __tableargs__ = {"comment": "Session"}

    number_participants = Column(name="number_participants", type_=Integer, comment="Number Participants")
    game_id = Column(
        ForeignKey("game.id", ondelete="NO ACTION"),
        nullable=False,
    )
    user_id = Column(
        ForeignKey("user.id", ondelete="NO ACTION"),
        nullable=False,
    )
    is_active = Column(name="is_active", type_=Boolean, comment="Game is active")
    is_finished = Column(name="is_finished", type_=Boolean, comment="Game is finished")

    def __repr__(self):
        return f"{self.game_id}"


class LinkGame(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "link_game"
    __tableargs__ = {"comment": "Link Game"}

    link = Column(name="link", type_=String(200), comment="Link for gamers")
    session_id = Column(
        ForeignKey("session.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.session_id}"
