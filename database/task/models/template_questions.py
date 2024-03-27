from sqlalchemy import Column, Text, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base
from database.game.models.game import Game
from database.task.models.questions import Question


class Template(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "template"
    __tableargs__ = {"comment": "Template"}

    name = Column(name="name", type_=Text, comment="Template name")
    team_number = Column(name="team_number", type_=Integer, comment="Team number", default=1)
    serial_number_question = Column(name="serial_number_question",
                                    type_=Integer,
                                    comment="Serial number question", default=1)
    game_id = Column(
        ForeignKey("game.id", ondelete="NO ACTION"),
        nullable=False,
    )
    question_id = Column(
        ForeignKey("question.id", ondelete="NO ACTION"),
        nullable=False,
    )
    game = relationship(Game, backref='templates')
    question = relationship(Question, backref='templates')

    def __repr__(self):
        return f"{self.name}"


# class TemplateQuestion(CreateMixin, SaveMixin, BaseMixin, Base):
#     __tablename__ = "template_question"
#     __tableargs__ = {"comment": "Template question"}
#
#     template_id = Column(
#         ForeignKey("template.id", ondelete="NO ACTION"),
#         nullable=False,
#     )
#     question_id = Column(
#         ForeignKey("question.id", ondelete="NO ACTION"),
#         nullable=False,
#     )
#     template = relationship(Template, backref='template_questions')
#     question = relationship(Question, backref='template_questions')
