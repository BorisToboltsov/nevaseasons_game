from typing import NoReturn

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from sqlalchemy.orm import Session

from services.commands.services_start import Start


router_commands = Router()


@router_commands.message(Command("start"))
async def commands_start(message: types.Message, state: FSMContext, session: Session) -> NoReturn:
    # print(1)
    # print(session)
    start = Start()
    await start.start(message, session)
