import uuid
from typing import NoReturn

from aiogram.types import CallbackQuery, Chat, Message, User
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.manager.bg_manager import BgManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.handlers.onboarding import router_onboarding
from bot.states.leader import FSMLeader
from bot.states.start_game import FSMStartGame
from database.task.crud.answers import DbAnswer
from services.task.task import Task


async def select_answer(
    callback: CallbackQuery, widget: Button, dialog_manager: DialogManager, item_id: str
):
    await check_answer(dialog_manager, callback)


async def message_handler(
    message: Message, widget: MessageInput, dialog_manager: DialogManager
) -> None:
    await check_answer(dialog_manager, message)


async def start_game(
    callback: CallbackQuery, button: Button, dialog_manager: DialogManager
) -> NoReturn:
    await distribution_dialog(dialog_manager)


async def distribution_dialog(dialog_manager: DialogManager, current_task: Task | None = None, **kwargs) -> NoReturn:
    templates = dialog_manager.start_data.get("templates")
    try:
        template = templates.pop(0)
    except IndexError:
        # Конец игры подсчет очков
        await dialog_manager.switch_to(state=FSMStartGame.end_game)
        return
    dialog_manager.dialog_data["templates"] = templates
    session = dialog_manager.middleware_data.get("session")
    db_answer = DbAnswer()
    answers_list = db_answer.get_answer_list_by_question(
        template.question_id, session=session
    )
    task = Task(template=template, answers_list=answers_list)
    dialog_manager.dialog_data["current_task"] = task

    dialog_manager.show_mode = ShowMode.AUTO  # Вот эту строку нужно добавить

    if task.template.question.type_response == 1:
        await dialog_manager.switch_to(state=FSMStartGame.choice)
    elif task.template.question.type_response == 2:
        await dialog_manager.switch_to(state=FSMStartGame.input_text)
    elif task.template.question.type_response == 3:
        await dialog_manager.switch_to(state=FSMStartGame.input_text_photo)


async def check_answer(dialog_manager: DialogManager, entity: CallbackQuery | Message) -> NoReturn:
    if type(entity) == Message:
        participant_answer = entity.text.lower()
    else:
        participant_answer = entity.data
        participant_answer = participant_answer.split(":")[1].lower()
    task = dialog_manager.dialog_data.get("current_task")
    dialog_manager.dialog_data["send_answer"] = True
    for answer in task.answers_list:
        if answer.is_correct:
            correct_answer = answer.answer_text.lower()

    # task.template.question.requires_verification = True  # TODO: Убрать!

    if task.template.question.requires_verification:
        # Если вопрос требует верификации у гида
        await dialog_manager.switch_to(state=FSMStartGame.wait)

        user_game = dialog_manager.start_data.get("game_session").user
        participant_game = dialog_manager.start_data.get("participant_game")

        user = User(id=user_game.telegram_id, is_bot=False, first_name="First name")
        chat = Chat(id=user_game.telegram_id, type="private")
        manager = BgManager(
            user=user,
            chat=chat,
            bot=entity.bot,
            router=router_onboarding,
            intent_id=None,
            stack_id=f"{uuid.uuid4()}",
        )
        bg = dialog_manager.bg()
        await manager.start(
            FSMLeader.first,
            mode=StartMode.NEW_STACK,
            show_mode=ShowMode.EDIT,
            data={
                "correct_answer": correct_answer,
                "participant_answer": participant_answer,
                "command_name": participant_game.command_name.name,
                "bg": bg,
                "current_task": task,
            },
        )
    else:
        if participant_answer == correct_answer:
            # Правильный ответ
            await dialog_manager.switch_to(state=FSMStartGame.start)
        else:
            # Не правильный ответ
            if task.template.question.type_response == 1:
                await dialog_manager.switch_to(state=FSMStartGame.choice_no_answer)
            elif task.template.question.type_response == 2:
                await dialog_manager.switch_to(state=FSMStartGame.input_text_no_answer)
            elif task.template.question.type_response == 3:
                await dialog_manager.switch_to(state=FSMStartGame.input_text_photo_no_answer)
