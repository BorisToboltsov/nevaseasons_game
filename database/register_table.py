from sqlalchemy import MetaData

from database.game.models.game import Game
from database.participant.models.participant import Participant, ParticipantGame
from database.session.models.game_session import GameSession, LinkGame
from database.task.models.answers import Answer
from database.task.models.template import Template
from database.task.models.questions import Question
from database.user.models.user import User

"""
Наименование index и constraint по умолчанию:
ix - обычный индекс
uq - уникальный индекс
fk - foreign key
pk - primary key
"""
convention = {
    "all_column_names": lambda constraint, table: "_".join(
        [column.name for column in constraint.columns.values()]
    ),
    "ix": "ix__%(table_name)s__%(all_column_names)s",
    "uq": "uq__%(table_name)s__%(all_column_names)s",
    "ck": "ck__%(table_name)s__%(constraint_name)s",
    "fk": ("fk__%(table_name)s__%(all_column_names)s__%(referred_table_name)s"),
    "pk": "pk__%(table_name)s",
}

metadata = MetaData(naming_convention=convention)

User()
Question()
Answer()
Game()
Template()
Participant()
ParticipantGame()
LinkGame()
GameSession()
