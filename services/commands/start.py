from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from bot.states.onboarding import FSMOnboarding
from database.participant.crud.participant import (
    DbCommandName,
    DbParticipant,
    DbParticipantGame,
)
from database.participant.models.participant import Participant, ParticipantGame
from database.session.crud.game_session import DbLinkGame
from database.user.crud.user import DbUser
from services.utils.utm_tag import UtmTag
from view.onboarding import (
    command_registration,
    command_registration_full,
    create_participant_game,
    create_participant_game_full,
    game_is_finished,
    invalid_link,
    participant_game_exist,
    send_phone,
)


class Start:
    def __init__(
        self, message: Message, session: Session, dialog_manager: DialogManager
    ):
        self.message = message
        self.session = session
        self.dialog_manager: DialogManager = dialog_manager

    async def start(self):
        utm_tag = UtmTag()
        await utm_tag.parse_utm_tag(self.message)
        if utm_tag.utm_tag:
            user_bot = await self.message.bot.get_me()
            bot_name = user_bot.username
            link = f"https://t.me/{bot_name}?start={utm_tag.utm_tag}"
            try:
                db_link_game = DbLinkGame()
                link_game = db_link_game.get_link_game_by_link(
                    link=link, session=self.session
                )
                game_session = link_game.game_session
            except NoResultFound:
                await invalid_link(self.message)
                return

            try:
                db_participant = DbParticipant()
                participant = db_participant.get_user_by_telegram(
                    session=self.session, telegram_id=self.message.from_user.id
                )
            except NoResultFound:
                participant = Participant(telegram_id=self.message.from_user.id)
                self.session.add(participant)
                self.session.commit()

            db_participant_game = DbParticipantGame()
            participant_game_is_exist = (
                db_participant_game.get_participant_game_by_gs_p(
                    session=self.session,
                    game_session_id=game_session.id,
                    participant_id=participant.id,
                )
            )
            if game_session.is_finished:
                await game_is_finished(self.message)
            elif participant_game_is_exist:
                await participant_game_exist(self.message)
            elif game_session.is_active:
                command_name = self._get_command_name()
                all_participant_game = (
                    db_participant_game.get_all_participant_game_by_game_session(
                        session=self.session, game_session_id=game_session.id
                    )
                )
                if all_participant_game:
                    for participant_game in all_participant_game:
                        command_name = self._get_command_name()
                        if participant_game.command_name.name == command_name:
                            continue
                        else:
                            participant_game = ParticipantGame(
                                participant_id=participant.id,
                                command_name_id=command_name.id,
                                game_session_id=game_session.id,
                                link_game_id=link_game.id,
                            )
                            self.session.add(participant_game)
                            break
                else:
                    participant_game = ParticipantGame(
                        participant_id=participant.id,
                        command_name_id=command_name.id,
                        game_session_id=game_session.id,
                        link_game_id=link_game.id,
                    )
                    self.session.add(participant_game)

                self.session.commit()

                # Проверка все команды созданы или еще нет?
                all_participant_game = (
                    db_participant_game.get_all_participant_game_by_game_session(
                        session=self.session, game_session_id=game_session.id
                    )
                )
                if len(all_participant_game) == game_session.number_participants:
                    for i, participant_game in enumerate(all_participant_game):
                        participant_game.sequence_number = i + 1
                        self.session.commit()
                    await create_participant_game_full(self.message, command_name.name)
                    await command_registration_full(
                        self.message, game_session.user.telegram_id, command_name.name
                    )
                else:
                    await create_participant_game(self.message, command_name.name)
                    await command_registration(
                        self.message,
                        game_session.user.telegram_id,
                        command_name.name,
                        len(all_participant_game),
                        game_session.number_participants,
                    )
        else:
            db_user = DbUser()
            try:
                user = db_user.get_user_by_telegram(
                    self.message.from_user.id, self.session
                )
                await self.dialog_manager.start(
                    state=FSMOnboarding.first,
                    mode=StartMode.RESET_STACK,
                    data={"user": user},
                )
            except NoResultFound:
                await send_phone(self.message)

    def _get_command_name(self):
        db_command_name = DbCommandName()
        return db_command_name.get_random_command_name(session=self.session)
