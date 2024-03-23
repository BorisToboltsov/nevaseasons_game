from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from bot.states.start import FSMStartGame


async def start_game_handler(callback: CallbackQuery,
                             widget: Button,
                             dialog_manager: DialogManager):
    await dialog_manager.next()


async def game_selection(callback: CallbackQuery,
                         widget: Button,
                         dialog_manager: DialogManager,
                         item_id: str):
    dialog_manager.dialog_data['game_id'] = item_id
    await dialog_manager.next()


async def error_command_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str):
    await message.answer(
        text='Необходимо ввести число, кол-во команд не больше 5. Попробуйте еще раз'
    )


def command_check(text: str) -> str:
    if all(ch.isdigit() for ch in text) and 1 <= int(text) <= 5:
        return text
    raise ValueError


async def correct_command_handler(
        message: Message,
        widget: ManagedTextInput,
        dialog_manager: DialogManager,
        text: str) -> None:
    dialog_manager.dialog_data['command_quantity'] = int(text)
    await dialog_manager.next()


async def quantity_no_handler(callback: CallbackQuery,
                              widget: Button,
                              dialog_manager: DialogManager) -> None:
    dialog_manager.dialog_data['command_quantity'] = 0
    await dialog_manager.switch_to(state=FSMStartGame.three)


async def quantity_yes_handler(
        callback: CallbackQuery,
        widget: Button,
        dialog_manager: DialogManager) -> None:
    dialog_manager.dialog_data['guide'] = callback.from_user.id
    print(dialog_manager.dialog_data)
