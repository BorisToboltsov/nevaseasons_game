from aiogram.enums import ContentType
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button, Column, Select
from aiogram_dialog.widgets.media import DynamicMedia
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.start_game.getters import get_task_choice, get_task_input, get_start_message
from bot.dialogs.start_game.handlers import message_handler, select_answer, start_game, input_photo
from bot.states.start_game import FSMStartGame

start_game_dialog = Dialog(
    Window(
        Format("{text}"),
        Button(text=Format("{button}"), id="button_1", on_click=start_game),
        state=FSMStartGame.start,
        getter=get_start_message,
    ),
    Window(
        DynamicMedia("image", when="path_to_image"),
        Format("Вопрос №{number_question}\n\n", when="not_send_answer"),
        Format("{question_text}"),
        Column(
            Select(
                Format("{item.answer_text}"),
                id="answer",
                item_id_getter=lambda x: x.answer_text,
                items="answers_list",
                on_click=select_answer,
            ),
        ),
        state=FSMStartGame.choice,
        getter=get_task_choice,
    ),
    Window(
        DynamicMedia("image", when="path_to_image"),
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
        DynamicMedia("image", when="path_to_image"),
        Format("Вопрос №{number_question}\n\n"),
        Format("{question_text}"),
        MessageInput(
            func=input_photo,
            content_types=ContentType.PHOTO,
        ),
        state=FSMStartGame.input_text_photo,
        getter=get_task_input,
    ),
    Window(
        Const("Ожидайте проверки ответа"),
        state=FSMStartGame.wait,
    ),
    Window(
        Const("Конец игры"),
        state=FSMStartGame.end_game,
    ),

    Window(
        DynamicMedia("image", when="path_to_image"),
        Const("Не верно! Попробуйте еще раз!\n"),
        Format("Вопрос №{number_question}\n\n", when="not_send_answer"),
        Format("{question_text}"),
        Column(
            Select(
                Format("{item.answer_text}"),
                id="answer",
                item_id_getter=lambda x: x.answer_text,
                items="answers_list",
                on_click=select_answer,
            ),
        ),
        state=FSMStartGame.choice_no_answer,
        getter=get_task_choice,
    ),
    Window(
        DynamicMedia("image", when="path_to_image"),
        Const("Не верно! Попробуйте еще раз!\n"),
        Format("Вопрос №{number_question}\n\n"),
        Format("{question_text}"),
        MessageInput(
            func=message_handler,
            content_types=ContentType.TEXT,
        ),
        state=FSMStartGame.input_text_no_answer,
        getter=get_task_input,
    ),
    Window(
        DynamicMedia("image", when="path_to_image"),
        Const("Не верно! Попробуйте еще раз!\n"),
        Format("Вопрос №{number_question}\n\n"),
        Format("{question_text}"),
        MessageInput(
            func=input_photo,
            content_types=ContentType.PHOTO,
        ),
        state=FSMStartGame.input_text_photo_no_answer,
        getter=get_task_input,
    ),
    Window(
        Format("Отправьте ответ\n"),
        MessageInput(
            func=message_handler,
            content_types=ContentType.TEXT,
        ),
        state=FSMStartGame.wait_answer,
    ),

)
