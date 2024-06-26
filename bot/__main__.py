import asyncio
import logging

import sentry_sdk
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from bot.dialogs.leader.dialog import leader_dialog
from bot.dialogs.onboarding.dialog import onboarding_dialog
from bot.dialogs.start_game.dialog import start_game_dialog
from bot.handlers.commands import router_commands
from bot.handlers.onboarding import router_onboarding
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
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher(storage=MemoryStorage())

    # Configure logging
    logging.basicConfig(level=logging.WARNING)

    # Router register
    dp.include_router(router_commands)
    dp.include_router(router_onboarding)

    # Dialog register
    dp.include_router(onboarding_dialog)
    dp.include_router(start_game_dialog)
    dp.include_router(leader_dialog)

    # Setup dialogs
    setup_dialogs(dp)

    # Middleware register
    dp.update.outer_middleware(Database(sm))

    # Start long polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
