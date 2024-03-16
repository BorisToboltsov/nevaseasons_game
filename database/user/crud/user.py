from typing import Type

from sqlalchemy.orm import Session

from database.user.models.user import User


class DbUser:

    @staticmethod
    def get_user_from_telegram(telegram_id: int, session: Session) -> Type[User]:
        return session.query(User).filter(User.telegram_id == telegram_id).one()
