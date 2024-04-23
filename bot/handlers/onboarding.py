import uuid
from typing import NoReturn

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Chat, Message, User
from aiogram_dialog import DialogManager, ShowMode, StartMode
from aiogram_dialog.manager.bg_manager import BgManager
from sqlalchemy.orm import Session

from bot.states.start_game import FSMStartGame
from database.participant.crud.participant import DbParticipantGame
from database.session.crud.game_session import DbGameSession
from database.task.crud.template import DbTemplate
from database.user.crud.user import DbUser
from services.onboarding.get_phone import GetPhone

router_onboarding = Router()


@router_onboarding.message(F.contact)
async def get_phone_handler(
    message: Message, session: Session, dialog_manager: DialogManager
) -> NoReturn:
    get_phone = GetPhone(message, session, dialog_manager)
    await get_phone.start()


@router_onboarding.callback_query(F.data == "Старт игры")
async def start_game_handler(
    message: Message, dialog_manager: DialogManager, state: FSMContext
) -> NoReturn:
    session = dialog_manager.middleware_data.get("session")

    db_user = DbUser()
    user = db_user.get_user_by_telegram(message.from_user.id, session=session)

    db_game_session = DbGameSession()
    game_session = db_game_session.get_game_session_by_user_id(user.id, session=session)

    db_participant_game = DbParticipantGame()
    participant_game_list = (
        db_participant_game.get_all_participant_game_by_game_session(
            game_session_id=game_session.id, session=session
        )
    )
    await state.update_data(game_session=game_session, user=user)

    for participant_game in participant_game_list:
        db_template = DbTemplate()
        templates_not_sort = db_template.get_task_list_by_template(
            session=session,
            game_id=game_session.game.id,
            team_number=participant_game.sequence_number,
        )
        templates = sorted(
            templates_not_sort, key=lambda x: x.serial_number_question, reverse=False
        )

        user = User(
            id=participant_game.participant.telegram_id,
            is_bot=False,
            first_name="First name",
        )
        chat = Chat(id=participant_game.participant.telegram_id, type="private")
        manager = BgManager(
            user=user,
            chat=chat,
            bot=message.bot,
            router=router_onboarding,
            intent_id=None,
            stack_id="",
        )

        await manager.start(
            FSMStartGame.start,
            mode=StartMode.NORMAL,
            show_mode=ShowMode.EDIT,
            data={
                "user": user,
                "game_session": game_session,
                "participant_game": participant_game,
                "participant": participant_game.participant,
                "templates": templates,
            },
        )
