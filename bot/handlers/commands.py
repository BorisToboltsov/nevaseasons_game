from typing import NoReturn

from aiogram import Router, types
from aiogram.filters import CommandStart
from sqlalchemy.orm import Session


router_commands = Router()


@router_commands.message(CommandStart())
async def commands_start(message: types.Message, session: Session) -> NoReturn:
    pass
