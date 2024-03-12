from sqlalchemy import Column, String, BigInteger, ForeignKey, Integer

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class Participant(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "participant"
    __tableargs__ = {"comment": "Participant"}

    username = Column(
        name="username", type_=String(100), comment="Telegram username, etc.")
    telegram_id = Column(name="telegram_id", type_=BigInteger, comment="Telegram id")

    def __repr__(self):
        return f"{self.id} {self.username}"


class ParticipantGame(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "participant_game"
    __tableargs__ = {"comment": "Participant Game"}

    participant_id = Column(
        ForeignKey("participant.id", ondelete="NO ACTION"),
        nullable=False,
    )
    game_id = Column(
        ForeignKey("game.id", ondelete="NO ACTION"),
        nullable=False,
    )
    score = Column(name="score", type_=Integer, comment="Score")
