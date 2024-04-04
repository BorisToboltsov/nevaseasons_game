from typing import NoReturn

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import DialogManager
from sqlalchemy.orm import Session

from bot.states.start_game import FSMStartGame
from database.participant.crud.participant import DbParticipantGame, DbParticipant


router_start_game = Router()


@router_start_game.callback_query(F.data == "Старт")
async def start_game_handler(callback_query: CallbackQuery,
                             session: Session,
                             dialog_manager: DialogManager,
                             state: FSMContext) -> NoReturn:
    db_participant = DbParticipant()
    participant = db_participant.get_user_by_telegram(callback_query.from_user.id, session=session)

    current_state = await state.get_data()
    user = current_state.get("user")
    game_session = current_state.get("game_session")

    db_participant_game = DbParticipantGame()
    participant_game = db_participant_game.get_participant_game_by_gs_p(session=session,
                                                                        participant_id=participant.id,
                                                                        game_session_id=game_session.id)

    await dialog_manager.start(state=FSMStartGame.first,
                               data={'user': user,
                                     'game_session': game_session,
                                     'participant_game': participant_game,
                                     'participant': participant})
