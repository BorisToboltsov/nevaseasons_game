from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from bot.states.start import FSMStartGame
from database.user.crud.user import DbUser
from view.onboarding import not_register, connect_success


class GetPhone:
    def __init__(self, message: Message, session: Session, dialog_manager: DialogManager):
        self.message = message
        self.session = session
        self.dialog_manager = dialog_manager

    async def start(self):
        contact = self.message.contact
        db_user = DbUser()
        await self.message.delete()  # Управление последнего сообщения
        await self.message.bot.delete_message(chat_id=self.message.chat.id, message_id=self.message.message_id - 1)  # Удаление предпоследнего сообщени
        try:
            user = db_user.get_user_by_phone(contact.phone_number, self.session)
            user.telegram_id = self.message.from_user.id
            self.session.commit()
            await connect_success(self.message)
            await self.dialog_manager.start(state=FSMStartGame.first, mode=StartMode.RESET_STACK, data={'user': user})
        except NoResultFound:
            await not_register(self.message)
