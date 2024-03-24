from typing import Type

from sqlalchemy.orm import Session

from database.session.models.gamesession import GameSession, LinkGame


class DbSession:

    @staticmethod
    def get_game_session_by_id(game_session_id: int, session: Session) -> Type[GameSession]:
        return session.query(GameSession).filter(GameSession.id == game_session_id).one()


class DbLinkGame:

    @staticmethod
    def get_link_game_by_link(link: str, session: Session) -> Type[LinkGame]:
        return session.query(LinkGame).filter(LinkGame.link == link).one()
