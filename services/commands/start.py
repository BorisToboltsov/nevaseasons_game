from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from bot.states.start import FSMStartGame
from database.user.crud.user import DbUser
from services.utils.utm_tag import UtmTag
from view.onboarding import send_phone


class Start:
    def __init__(self, message: Message, session: Session, dialog_manager: DialogManager):
        self.message = message
        self.session = session
        self.dialog_manager: DialogManager = dialog_manager

    async def start(self):
        utm_tag = UtmTag()
        await utm_tag.parse_utm_tag(self.message)
        if utm_tag.utm_tag:
            bot_name = self.message.message.from_user.username
            link = f'https://t.me/{bot_name}?start={utm_tag.utm_tag}'


        else:
            db_user = DbUser()
            try:
                user = db_user.get_user_by_telegram(self.message.from_user.id, self.session)
                await self.dialog_manager.start(state=FSMStartGame.first, mode=StartMode.RESET_STACK, data={'user': user})
            except NoResultFound:
                await send_phone(self.message)
