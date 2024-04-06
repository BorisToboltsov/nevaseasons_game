from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Update
from sqlalchemy.orm import sessionmaker


class Database(BaseMiddleware):
    def __init__(self, sm: sessionmaker) -> None:
        self.Session = sm

    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        data["session"] = self.Session()
        return await handler(event, data)
