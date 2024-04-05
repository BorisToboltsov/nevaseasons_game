from aiogram.types import CallbackQuery, Message, User, Chat
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.manager.bg_manager import BgManager
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Button

from bot.handlers.onboarding import router_onboarding
from bot.states.leader import FSMLeader
from bot.states.start_game import FSMStartGame
from database.task.crud.answers import DbAnswer
from services.task.task import Task


async def select_answer(callback: CallbackQuery,
                        widget: Button,
                        dialog_manager: DialogManager,
                        item_id: str):
    participant_answer = callback.data
    task = dialog_manager.dialog_data.get('current_task')
    dialog_manager.dialog_data['send_answer'] = True
    for answer in task.answers_list:
        if answer.is_correct:
            correct_answer = answer

    participant_answer = participant_answer.split(':')[1]

    task.template.question.requires_verification = True  # TODO: Убрать!

    if task.template.question.requires_verification:
        user_game = dialog_manager.start_data.get('game_session').user
        participant_game = dialog_manager.start_data.get('participant_game')

        user = User(id=user_game.telegram_id, is_bot=False, first_name="First name")
        chat = Chat(id=user_game.telegram_id, type="private")
        manager = BgManager(user=user,
                            chat=chat,
                            bot=callback.bot,
                            router=router_onboarding,
                            intent_id=None, stack_id="")
        bg = dialog_manager.bg()

        await manager.start(FSMLeader.first,
                            mode=StartMode.NORMAL,
                            show_mode=ShowMode.EDIT,
                            data={'correct_answer': correct_answer.answer_text,
                                  'participant_answer': participant_answer,
                                  'command_name': participant_game.command_name.name,
                                  'bg': bg
                                  }
                            )

    else:
        if participant_answer == correct_answer.answer_text:
            print('Правильно!')
        else:
            print('Не правильно')


async def message_handler(message: Message,
                          widget: MessageInput,
                          dialog_manager: DialogManager) -> None:
    pass
    # if all(ch.isdigit() for ch in text) and 3 <= int(text) <= 120:
    #     return text
    # raise ValueError


async def start_game(callback: CallbackQuery, button: Button, dialog_manager: DialogManager):
    if dialog_manager.dialog_data.get('current_task') is None:
        print(dialog_manager.current_stack())
        templates = dialog_manager.start_data.get('templates')
        template = templates.pop(0)

        session = dialog_manager.middleware_data.get('session')
        db_answer = DbAnswer()
        answers_list = db_answer.get_answer_list_by_question(template.question_id, session=session)

        task = Task(template=template, answers_list=answers_list)
        dialog_manager.dialog_data['current_task'] = task
    else:
        task = dialog_manager.dialog_data.get('current_task')

    dialog_manager.show_mode = ShowMode.AUTO  # Вот эту строку нужно добавить

    if task.template.question.type_response == 1:
        await dialog_manager.switch_to(state=FSMStartGame.choice)
    elif task.template.question.type_response == 2:
        await dialog_manager.switch_to(state=FSMStartGame.input_text)
    elif task.template.question.type_response == 3:
        await dialog_manager.switch_to(state=FSMStartGame.input_text_photo)
