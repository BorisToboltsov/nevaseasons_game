from typing import NoReturn

from aiogram.types import Message
from sqlalchemy.orm import Session

from database.user.crud.user import DbUser


class Start:
    @staticmethod
    async def start(message: Message, session: Session) -> NoReturn:
        user = DbUser.get_user_from_telegram(message.from_user.id, session)
        print(type(user))
        print(user)
