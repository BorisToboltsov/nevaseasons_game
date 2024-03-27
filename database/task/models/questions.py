from sqlalchemy import Column, String, Text, Boolean, Integer

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class Question(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "question"
    __tableargs__ = {"comment": "Question"}

    text = Column(name="text", type_=Text, comment="Question text")
    explanation = Column(
        name="explanation", type_=Text, nullable=True, comment="Explanation"
    )
    path_explanation_image = Column(
        name="path_explanation_image",
        type_=String(100),
        nullable=True,
        comment="Path to explanation image",
    )
    path_image = Column(name="path_image", type_=String(100), comment="Path to image", nullable=True)
    multi_answer = Column(name="multi_answer", type_=Boolean, comment="Multi answer", default=False, nullable=True)
    requires_verification = Column(name="requires_verification", type_=Boolean, comment="Requires verification", default=False)
    type_response = Column(name="type_response",
                           type_=Integer,
                           comment="Type of response, 1-choice, 2-input text, 3-input photo +text")

    def __repr__(self):
        return f"{self.text}"
