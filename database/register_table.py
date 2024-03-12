from sqlalchemy import MetaData

from database.entity_language.model.entity_language import EntityLanguage
from database.entity_language.model.event import Event
from database.entity_language.model.language import Language
from database.entity_task.model.answer_text import AnswerText
from database.entity_task.model.answers import Answers
from database.entity_task.model.question_text import QuestionText
from database.entity_task.model.questions import Questions
from database.filter.model.template_filter_questions import TemplateFilterQuestions
from database.filter.model.users_filter_questions import UsersFilterQuestions
from database.profile.model.account import Account
from database.profile.model.profile import Profile
from database.profile.model.user_responses import ProfileAnswers

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

Language()
AnswerText()
QuestionText()
Answers()
Questions()
Event()
Account()
Profile()
ProfileAnswers()
UsersFilterQuestions()
EntityLanguage()
TemplateFilterQuestions()
