from sqlalchemy import Column, Text, ForeignKey

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class Template(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "template"
    __tableargs__ = {"comment": "Template"}

    name = Column(name="name", type_=Text, comment="Template name")
    game_id = Column(
        ForeignKey("game.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.name}"


class TemplateQuestion(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "template_question"
    __tableargs__ = {"comment": "Template question"}

    template_id = Column(
        ForeignKey("template.id", ondelete="NO ACTION"),
        nullable=False,
    )
    question_id = Column(
        ForeignKey("question.id", ondelete="NO ACTION"),
        nullable=False,
    )
