from sqlalchemy import Boolean, Column, ForeignKey, Text
from sqlalchemy.orm import relationship

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class Answer(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "answer"
    __tableargs__ = {"comment": "Answer"}

    answer_text = Column(name="answer_text", type_=Text, comment="Answer text")
    is_correct = Column(name="is_correct", type_=Boolean, comment="is correct")
    question_id = Column(
        ForeignKey("question.id", ondelete="NO ACTION"),
        nullable=False,
    )
    question = relationship("Question", backref="question")

    def __repr__(self):
        return f"{self.id}"
