from aiogram.types import Message
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from database.user.crud.user import DbUser
from view.onboarding import send_phone


class Start:
    def __init__(self, message: Message, session: Session):
        self.message = message
        self.session = session

    async def start(self):
        db_user = DbUser()
        try:
            user = db_user.get_user_from_telegram(self.message.from_user.id, self.session)
            # user.fio = 'Борис Олегович'
            # self.session.commit()
        except NoResultFound:
            await send_phone(self.message)
