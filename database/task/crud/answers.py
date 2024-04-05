from typing import Type

from sqlalchemy.orm import Session

from database.task.models.answers import Answer


class DbAnswer:

    @staticmethod
    def get_answer_list_by_question(question_id: int, session: Session) -> list[Type[Answer]]:
        return session.query(Answer).filter(Answer.question_id == question_id).all()
