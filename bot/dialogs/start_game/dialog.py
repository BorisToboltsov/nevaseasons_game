from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button, Select, Column
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.start_game.getters import get_game
from bot.dialogs.start_game.handlers import start_game_handler
from bot.states.start import FSMStartGame

start_game_dialog = Dialog(
    Window(
        Const(text='Можно начинать новую игру!'),
        Button(
            text=Const('Начать игру!'),
            id='start_game',
            on_click=start_game_handler),
        state=FSMStartGame.first
    ),
    Window(
        Const(text='Выберите игру.'),
        Column(
            Select(
                Format('{item.name}'),
                id='categ',
                item_id_getter=lambda x: x.id,
                items='game_list'
            ),
        ),
        getter=get_game,
        state=FSMStartGame.two
    ),
)
