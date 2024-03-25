from sqlalchemy.orm import Session

from database.game.models.game import Game
from services.init_database.print_message_decorator import print_message


class InitDbSaveGame:
    def __init__(self, session: Session):
        self.game_list = [
            "Александрийский сад",
            "Новая Голландия",
            "ППК",
        ]
        self.session = session

    @print_message("Start add game", "Complete add game\n")
    def write_game(self):
        for game in self.game_list:
            # Создаем новую запись.
            data = Game(
                name=game,
            )
            self.session.add(data)
        return self.session
