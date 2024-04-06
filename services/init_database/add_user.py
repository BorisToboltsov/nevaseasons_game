from sqlalchemy.orm import Session

from database.user.models.user import User
from services.init_database.print_message_decorator import print_message


class InitDbUser:
    def __init__(self, session: Session):
        self.user_list = [
            {
                "fio": "Тобольцов Борис Олегович",
                "phone_number": 79819701757,
                "telegram_id": 446998054,
                "is_active": True,
            }
        ]
        self.session = session

    @print_message("Start add user", "Complete add user\n")
    def write_user(self):
        for user in self.user_list:
            # Создаем новую запись.
            data = User(
                fio=user.get("fio"),
                phone_number=user.get("phone_number"),
                telegram_id=user.get("telegram_id"),
                is_active=user.get("is_active"),
            )
            self.session.add(data)
        return self.session
