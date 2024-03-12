from sqlalchemy import Column, Text, ForeignKey

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class Group(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "group"
    __tableargs__ = {"comment": "Group"}

    name = Column(name="name", type_=Text, comment="group name")
    game_id = Column(
        ForeignKey("game.id", ondelete="NO ACTION"),
        nullable=False,
    )

    def __repr__(self):
        return f"{self.name}"


class GroupQuestion(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "group_question"
    __tableargs__ = {"comment": "Group question"}

    group_id = Column(
        ForeignKey("group.id", ondelete="NO ACTION"),
        nullable=False,
    )
    question_id = Column(
        ForeignKey("question.id", ondelete="NO ACTION"),
        nullable=False,
    )
