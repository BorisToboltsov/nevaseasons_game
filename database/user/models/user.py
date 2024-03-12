from sqlalchemy import Column, ForeignKey, String
from sqlalchemy_utils import EmailType
from sqlalchemy.orm import relationship

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class User(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "profile"
    __tableargs__ = {"comment": "Profile"}

    username = Column(
        name="username", type_=String(100), comment="Telegram username, etc.")
    email = Column(name="email", type_=EmailType, comment="Email")
    phone_number = Column(name="phone_number", type_=String(11), comment="Phone number")

    def __repr__(self):
        return f"{self.id} {self.username}"
