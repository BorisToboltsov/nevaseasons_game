from typing import NoReturn

from aiogram import Router, F
from aiogram.types import Message
from aiogram_dialog import DialogManager
from sqlalchemy.orm import Session

from services.onboarding.get_phone import GetPhone

router_onboarding = Router()


@router_onboarding.message(F.contact)
async def get_phone_handler(message: Message, session: Session, dialog_manager: DialogManager) -> NoReturn:
    get_phone = GetPhone(message, session, dialog_manager)
    await get_phone.start()
