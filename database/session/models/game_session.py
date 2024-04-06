from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base
from database.game.models.game import Game
from database.user.models.user import User


class GameSession(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "game_session"
    __tableargs__ = {"comment": "Game session"}

    number_participants = Column(
        name="number_participants", type_=Integer, comment="Number Participants"
    )
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
    user = relationship(User, backref="game_sessions")
    game = relationship(Game, backref="game_sessions")

    def __repr__(self):
        return f"{self.game_id}"


class LinkGame(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "link_game"
    __tableargs__ = {"comment": "Link Game"}

    link = Column(name="link", type_=String(200), comment="Link for gamers")
    game_session_id = Column(
        ForeignKey("game_session.id", ondelete="NO ACTION"),
        nullable=False,
    )
    game_session = relationship(GameSession, backref="link_games")

    def __repr__(self):
        return f"{self.game_session_id}"
