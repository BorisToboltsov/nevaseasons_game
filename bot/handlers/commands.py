from typing import NoReturn

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram_dialog import DialogManager
from sqlalchemy.orm import Session

from services.commands.start import Start

router_commands = Router()


@router_commands.message(CommandStart())
async def commands_start(
    message: Message, session: Session, dialog_manager: DialogManager
) -> NoReturn:
    start = Start(message, session, dialog_manager)
    await start.start()
