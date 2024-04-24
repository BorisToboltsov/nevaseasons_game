from typing import NoReturn

from aiogram.types import Message, CallbackQuery


async def command_end_game(callback: CallbackQuery, user_telegram_id: int, command_name: str, current_quantity, total_number) -> NoReturn:
    context = f"Команда {command_name}, закончила игру. {current_quantity} из {total_number}"
    await callback.bot.send_message(
        user_telegram_id, context
    )


async def all_commands_end_game(
    message: Message, user_telegram_id: int, command_name: str
) -> NoReturn:
    context = f"Команда {command_name}, закончила игру. Все команды закончили игру!\nПоздравляю, Вам повезло, бот не упал! "
    await message.bot.send_message(
        user_telegram_id, context)


async def command_win(callback: CallbackQuery, user_telegram_id: int, command_name: str, current_quantity, total_number) -> NoReturn:
    context = f"Команда {command_name}, закончила игру. {current_quantity} из {total_number}\nЭто победитель!"
    await callback.bot.send_message(
        user_telegram_id, context
    )
