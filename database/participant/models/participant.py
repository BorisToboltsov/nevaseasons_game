from sqlalchemy import Column, String, BigInteger, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base
from database.session.models.gamesession import GameSession, LinkGame


class Participant(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "participant"
    __tableargs__ = {"comment": "Participant"}

    telegram_id = Column(name="telegram_id", type_=BigInteger, comment="Telegram id")

    def __repr__(self):
        return f"{self.id} {self.telegram_id}"


class CommandName(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "command_name"
    __tableargs__ = {"comment": "Command name"}

    name = Column(
        name="name", type_=String(100), comment="Command name")

    def __repr__(self):
        return f"{self.id} {self.name}"


class ParticipantGame(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "participant_game"
    __tableargs__ = {"comment": "Participant Game"}

    score = Column(name="score", type_=Integer, comment="Score", default=0)
    participant_id = Column(
        ForeignKey("participant.id", ondelete="NO ACTION"),
        nullable=False,
    )
    game_session_id = Column(
        ForeignKey("game_session.id", ondelete="NO ACTION"),
        nullable=False,
    )
    command_name_id = Column(
        ForeignKey("command_name.id", ondelete="NO ACTION"),
        nullable=False,
    )
    link_game_id = Column(
        ForeignKey("link_game.id", ondelete="NO ACTION"),
        nullable=False,
    )

    participant = relationship(Participant, backref='participant_games')
    game_session = relationship(GameSession, backref='participant_games')
    link_game = relationship(LinkGame, backref='participant_games')
    command_name = relationship(CommandName, backref='participant_games')
