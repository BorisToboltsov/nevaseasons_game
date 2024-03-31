from typing import Type

from sqlalchemy.orm import Session

from database.session.models.game_session import GameSession, LinkGame


class DbGameSession:

    @staticmethod
    def get_game_session_by_id(game_session_id: int, session: Session) -> Type[GameSession]:
        return session.query(GameSession).filter(GameSession.id == game_session_id).one()

    @staticmethod
    def get_game_session_by_user_id(user_id: int, session: Session) -> Type[GameSession]:
        return session.query(GameSession).filter(GameSession.user_id == user_id,
                                                 GameSession.is_active.is_(True)).one()


class DbLinkGame:

    @staticmethod
    def get_link_game_by_link(link: str, session: Session) -> Type[LinkGame]:
        return session.query(LinkGame).filter(LinkGame.link == link).one()
