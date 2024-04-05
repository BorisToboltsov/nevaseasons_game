from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Select
from aiogram_dialog.widgets.text import Format

from bot.dialogs.start_game.getters import get_task
from bot.dialogs.start_game.handlers import select_answer
from bot.states.start_game import FSMStartGame

start_game_dialog = Dialog(
    Window(
        Format('Вопрос №{number_question}\n\n'),
        Format('{question_text}'),
        Select(
            Format('{item.answer_text}'),
            id='answer',
            item_id_getter=lambda x: x.id,
            items='answers_list',
            on_click=select_answer,
        ),
        state=FSMStartGame.first,
        getter=get_task,
    ),
    Window(
        Format('Вопрос №{number_question}\n\n'),
        Format('{question_text}'),
        TextInput(
            id='age_input',
            type_factory=age_check,
            on_success=correct_age_handler,
            on_error=error_age_handler,
        ),
        state=FSMStartGame.two,
        getter=get_task,
    ),
)
