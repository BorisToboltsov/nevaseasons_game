import asyncio
import logging
import os

import sentry_sdk
from dotenv import load_dotenv

from telegram_bot.connect import bot, dp
from telegram_bot.handlers.commands.commands_handlers import router_commands
from telegram_bot.handlers.message.message_handlers import router_message
from telegram_bot.handlers.poll_answers.poll_answers_handlers import router_poll_answers


async def main():
    load_dotenv()

    # Configure Sentry
    sentry_sdk.init(os.getenv("API_TOKEN_SENTRY"))

    # Configure logging
    logging.basicConfig(level=logging.WARNING)

    # Router register
    dp.include_router(router_commands)

    # Start long polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
