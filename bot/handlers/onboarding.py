from typing import NoReturn

from aiogram import Router, F
from aiogram.types import Message
from sqlalchemy.orm import Session

from services.onboarding.get_phone import GetPhone

router_onboarding = Router()


@router_onboarding.message(F.contact)
async def get_phone_handler(message: Message, session: Session) -> NoReturn:
    get_phone = GetPhone(message, session)
    await get_phone.start()
