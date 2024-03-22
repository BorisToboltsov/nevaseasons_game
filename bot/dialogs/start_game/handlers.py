from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button


async def start_game_handler(callback: CallbackQuery,
                             widget: Button,
                             dialog_manager: DialogManager):
    await dialog_manager.next()
