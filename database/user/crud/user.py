from typing import Type

from sqlalchemy.orm import Session

from database.user.models.user import User


class DbUser:

    @staticmethod
    def get_user_by_telegram(telegram_id: int, session: Session) -> Type[User]:
        return session.query(User).filter(User.telegram_id == telegram_id).one()

    @staticmethod
    def get_user_by_phone(phone_number: str, session: Session) -> Type[User]:
        return session.query(User).filter(User.phone_number == phone_number).one()
