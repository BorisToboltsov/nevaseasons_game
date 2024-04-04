from typing import Type

from sqlalchemy.orm import Session

from database.game.models.game import Game


class DbGame:

    @staticmethod
    def get_all_game(session: Session) -> list:
        return session.query(Game).filter(Game.is_active.is_(True)).all()

    @staticmethod
    def get_game_by_name(session: Session, name: str) -> Type[Game]:
        return session.query(Game).filter(Game.name == name).one()
