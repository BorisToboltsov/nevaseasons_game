from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from bot.states.start_game import FSMStartGame


async def button_yes(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    bg = dialog_manager.start_data.get("bg")
    await bg.switch_to(state=FSMStartGame.start)
    await dialog_manager.done()


async def button_no(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    pass
