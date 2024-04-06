from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Column, Select
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.start_game.getters import get_task_choice, get_task_input
from bot.dialogs.start_game.handlers import message_handler, select_answer, start_game
from bot.states.start_game import FSMStartGame

start_game_dialog = Dialog(
    Window(
        Const("Нажми старт"),
        Button(text=Const("Старт"), id="button_1", on_click=start_game),
        state=FSMStartGame.distribution,
    ),
    Window(
        Format("Вопрос №{number_question}\n\n", when="not_send_answer"),
        Format("{question_text}", when="not_send_answer"),
        Const("Ожидайте проверки ответа", when="send_answer"),
        Column(
            Select(
                Format("{item.answer_text}"),
                id="answer",
                item_id_getter=lambda x: x.answer_text,
                items="answers_list",
                on_click=select_answer,
                when="not_send_answer",
            ),
        ),
        state=FSMStartGame.choice,
        getter=get_task_choice,
    ),
    Window(
        Format("Вопрос №{number_question}\n\n"),
        Format("{question_text}"),
        MessageInput(
            func=message_handler,
            content_types=ContentType.TEXT,
        ),
        state=FSMStartGame.input_text,
        getter=get_task_input,
    ),
    Window(
        Format("Вопрос №{number_question}\n\n"),
        Format("{question_text}"),
        MessageInput(
            func=message_handler,
            content_types=ContentType.TEXT,
        ),
        state=FSMStartGame.input_text_photo,
        getter=get_task_input,
    ),
    Window(
        Const("Тест"),
        state=FSMStartGame.test,
    ),
)
