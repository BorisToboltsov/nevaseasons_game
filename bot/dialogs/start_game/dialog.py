from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Select, Column
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.start_game.getters import get_game, get_command_quantity
from bot.dialogs.start_game.handlers import start_game_handler, game_selection, error_command_handler, command_check, \
    correct_command_handler, quantity_yes_handler, quantity_no_handler
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
                items='game_list',
                on_click=game_selection,
            ),
        ),
        getter=get_game,
        state=FSMStartGame.two
    ),
    Window(
        Const(text='Какое количество команд участвует?'),
        TextInput(
            id='command_quantity_input',
            type_factory=command_check,
            on_success=correct_command_handler,
            on_error=error_command_handler,
        ),
        state=FSMStartGame.three,
    ),
    Window(
        Format('Участвует {command_quantity} команды, подтверждаете?'),
        Button(
            text=Const('Да'),
            id='choice_command_quantity_yes',
            on_click=quantity_yes_handler),
        Button(
            text=Const('Нет'),
            id='choice_command_quantity_no',
            on_click=quantity_no_handler),
        getter=get_command_quantity,
        state=FSMStartGame.four,
    ),
)
