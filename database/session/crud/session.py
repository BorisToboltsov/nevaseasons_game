class DbSession:

    @staticmethod
    def get_user_by_telegram(telegram_id: int, session: Session) -> Type[Session]:
        return session.query(Session).filter(Session.telegram_id == telegram_id).one()