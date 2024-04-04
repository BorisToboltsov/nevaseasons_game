from typing import Type

from sqlalchemy.orm import Session

from database.task.models.template import Template


class DbTemplate:

    @staticmethod
    def get_task_list_by_template(game_id: int, team_number: int, session: Session) -> list[Type[Template]]:
        return session.query(Template).filter(Template.game_id == game_id, Template.team_number == team_number).all()
