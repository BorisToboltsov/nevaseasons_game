from sqlalchemy.orm import Session

from database.game.models.game import Game


class DbGame:

    @staticmethod
    def get_all_game(session: Session) -> list:
        return session.query(Game).filter(Game.is_active.is_(True)).all()
