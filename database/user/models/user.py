from sqlalchemy import Column, String, BigInteger
from sqlalchemy_utils import EmailType

from database.base.mixin.base_mixin import BaseMixin, CreateMixin, SaveMixin
from database.base.model.base import Base


class User(CreateMixin, SaveMixin, BaseMixin, Base):
    __tablename__ = "user"
    __tableargs__ = {"comment": "User"}

    fio = Column(
        name="fio", type_=String(100), comment="Fio")
    email = Column(name="email", type_=EmailType, comment="Email")
    phone_number = Column(name="phone_number", type_=String(11), comment="Phone number")
    telegram_id = Column(name="telegram_id", type_=BigInteger, comment="Telegram id")

    def __repr__(self):
        return f"{self.id} {self.fio}"
