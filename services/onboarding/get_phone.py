from aiogram.types import Message
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from database.user.crud.user import DbUser
from view.onboarding import not_register, connect_success


class GetPhone:
    def __init__(self, message: Message, session: Session):
        self.message = message
        self.session = session

    async def start(self):
        contact = self.message.contact
        db_user = DbUser()
        try:
            user = db_user.get_user_by_phone(contact.phone_number, self.session)
            user.telegram_id = self.message.from_user.id
            self.session.commit()
            await connect_success(self.message)

        except NoResultFound:
            await not_register(self.message)
