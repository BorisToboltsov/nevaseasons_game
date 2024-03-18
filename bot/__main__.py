import asyncio
import logging

import sentry_sdk
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.handlers.commands import router_commands
from bot.middlewares.database import Database
from config.config import Config, load_config
from config.database import load_database


async def main():
    # Load config
    config: Config = load_config()
    database_config = load_database()

    # Configure Sentry
    sentry_sdk.init(config.sentry.token)

    sm = database_config.get_sessionmaker

    # Init telegram bot
    bot = Bot(token=config.tg_bot.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    # Configure logging
    logging.basicConfig(level=logging.WARNING)

    # Router register
    dp.include_router(router_commands)

    # Middleware register
    dp.update.outer_middleware(Database(sm))

    # Start long polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
