from typing import NoReturn

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy.orm import Session

from services.commands.start import Start

router_commands = Router()


@router_commands.message(CommandStart())
async def commands_start(message: Message, session: Session) -> NoReturn:
    start = Start(message, session)
    await start.start()
