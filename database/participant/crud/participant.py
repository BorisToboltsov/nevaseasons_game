from typing import Type

from sqlalchemy import func
from sqlalchemy.orm import Session

from database.participant.models.participant import (
    CommandName,
    Participant,
    ParticipantGame,
)


class DbParticipant:

    @staticmethod
    def get_user_by_telegram(telegram_id: int, session: Session) -> Type[Participant]:
        return (
            session.query(Participant)
            .filter(Participant.telegram_id == telegram_id)
            .one()
        )


class DbCommandName:

    @staticmethod
    def get_random_command_name(session: Session) -> Type[CommandName]:
        return session.query(CommandName).order_by(func.random()).first()


class DbParticipantGame:

    @staticmethod
    def get_participant_game_by_gs_p(
        game_session_id: int, participant_id: int, session: Session
    ) -> list[Type[ParticipantGame]]:
        return (
            session.query(ParticipantGame)
            .filter(
                ParticipantGame.game_session_id == game_session_id,
                ParticipantGame.participant_id == participant_id,
            )
            .one()
        )

    @staticmethod
    def get_all_participant_game_by_game_session(
        game_session_id: int, session: Session
    ) -> list[Type[ParticipantGame]]:
        return (
            session.query(ParticipantGame)
            .filter(ParticipantGame.game_session_id == game_session_id)
            .all()
        )

    @staticmethod
    def get_all_participant_game_complete(
        game_session_id: int, session: Session
    ) -> list[Type[ParticipantGame]]:
        return (
            session.query(ParticipantGame)
            .filter(ParticipantGame.game_session_id == game_session_id, ParticipantGame.is_active.is_(False))
            .all()
        )
