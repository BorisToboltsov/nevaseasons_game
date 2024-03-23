from pprint import pprint

from aiogram.types import CallbackQuery, Message
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.input import ManagedTextInput
from aiogram_dialog.widgets.kbd import Button

from bot.states.start import FSMStartGame
from database.session.models.session import Session, LinkGame
from services.start_game.link_generation import link_generation


async def start_game_handler(callback: CallbackQuery,
                             widget: Button,
                             dialog_manager: DialogManager):
    dialog_manager.dialog_data['user'] = dialog_manager.start_data.get('user')
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
        text='Необходимо ввести число, кол-во команд не больше 4. Попробуйте еще раз'
    )


def command_check(text: str) -> str:
    if all(ch.isdigit() for ch in text) and 1 <= int(text) <= 4:
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
    session = dialog_manager.middleware_data.get('session')
    game_session = Session(number_participants=dialog_manager.dialog_data['command_quantity'],
                           game_id=dialog_manager.dialog_data['game_id'],
                           user_id=dialog_manager.dialog_data['user'].id,
                           is_active=True,
                           is_finished=False)
    dialog_manager.dialog_data['game_session'] = game_session
    session.add(game_session)
    session.flush()

    bot_name = dialog_manager.middleware_data.get('event_update').callback_query.message.from_user.username
    command_quantity = dialog_manager.dialog_data['command_quantity']
    link_list = await link_generation(bot_name, command_quantity)
    dialog_manager.dialog_data['link_list'] = link_list

    for link in link_list:
        link_game = LinkGame(link=link,
                             session_id=game_session.id)
        session.add(link_game)
    session.commit()

    await dialog_manager.next()
