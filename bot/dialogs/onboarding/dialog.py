from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Button, Select, Column, Row
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.onboarding.getters import get_game, get_command_quantity, get_data
from bot.dialogs.onboarding.handlers import start_game_handler, game_selection, error_command_handler, command_check, \
    correct_command_handler, quantity_yes_handler, quantity_no_handler, go_next, go_back
from bot.states.onboarding import FSMOnboarding

onboarding_dialog = Dialog(
    Window(
        Const(text='Можно начинать новую игру!'),
        Button(
            text=Const('Начать игру!'),
            id='start_onboarding',
            on_click=start_game_handler),
        state=FSMOnboarding.first
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
        state=FSMOnboarding.two
    ),
    Window(
        Const(text='Какое количество команд участвует?'),
        TextInput(
            id='command_quantity_input',
            type_factory=command_check,
            on_success=correct_command_handler,
            on_error=error_command_handler,
        ),
        state=FSMOnboarding.three,
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
        state=FSMOnboarding.four,
    ),
    Window(
        DynamicMedia("photo"),
        Format('Команда №{text}'),
        Row(
            Button(Const('◀️ Назад'), id='b_back', on_click=go_back),
            Button(Const('Вперед ▶️'), id='b_next', on_click=go_next),
        ),
        state=FSMOnboarding.five,
        getter=get_data,
    ),
)
