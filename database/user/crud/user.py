from database.connect_db import engine, get_session
from database.user.models.user import User

session = get_session(engine)


class DbUser:
    pass
    @staticmethod
    def get_profile(telegram_id: int) -> User:
        return session.query(User).filter(User.telegram_id == telegram_id).one()
