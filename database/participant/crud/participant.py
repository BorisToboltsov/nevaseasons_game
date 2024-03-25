from typing import Type

from sqlalchemy.orm import Session

from database.participant.models.participant import Participant


class DbParticipant:

    @staticmethod
    def get_user_by_telegram(telegram_id: int, session: Session) -> Type[Participant]:
        return session.query(Participant).filter(Participant.telegram_id == telegram_id).one()
