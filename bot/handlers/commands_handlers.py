from typing import NoReturn

from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from services.commands.services_start import Start

router_commands = Router()


@router_commands.message(Command("start"))
async def commands_start(message: types.Message, state: FSMContext) -> NoReturn:
    start = Start()
    await start.start(message)
