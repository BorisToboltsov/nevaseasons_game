from typing import NoReturn

from aiogram.types import Message

from bot.keyboards.inline_keyboard import get_inline_keyboard
from bot.keyboards.markup_keyboard import get_markup_keyboard, keyboard_remove


async def send_phone(message: Message) -> NoReturn:
    context = "Чтобы идентифицировать вас, нам необходим ваш номер телефона. Нажмите на кнопку ниже."
    await message.bot.send_message(
        message.from_user.id,
        context,
        reply_markup=get_markup_keyboard("Отправить номер телефона", True),
    )


async def not_register(message: Message) -> NoReturn:
    context = "Вы не зарегистрированы. Обратитесь в ОРП."
    await message.bot.send_message(
        message.from_user.id, context, reply_markup=keyboard_remove()
    )


async def connect_success(message: Message) -> NoReturn:
    context = "Поздравляем вы подключены к игре в качестве ведущего."
    await message.bot.send_message(
        message.from_user.id, context, reply_markup=keyboard_remove()
    )


async def game_is_finished(message: Message) -> NoReturn:
    context = "Игра закончена!"
    await message.bot.send_message(
        message.from_user.id, context, reply_markup=keyboard_remove()
    )


async def invalid_link(message: Message) -> NoReturn:
    context = "Не верная ссылка. Нужно чтобы ведущий создал игру."
    await message.bot.send_message(
        message.from_user.id, context, reply_markup=keyboard_remove()
    )


async def participant_game_exist(message: Message) -> NoReturn:
    context = "Вы уже добавлены в игру, ожидайте начала."
    await message.bot.send_message(
        message.from_user.id, context, reply_markup=keyboard_remove()
    )


async def create_participant_game(message: Message, command_name: str) -> NoReturn:
    context = f"Итак, вы и ваша команда - {command_name}.\nПоздравляем...\nИ да, название поменять нельзя, сегодня вы {command_name}...\nПодтолкните своих противников, чтобы они быстрее регались."
    await message.bot.send_message(
        message.from_user.id, context, reply_markup=keyboard_remove()
    )


async def command_registration(
    message: Message,
    user_telegram_id: int,
    command_name: str,
    current_quantity: int,
    total_number: int,
) -> NoReturn:
    context = f"Команда {command_name}, зарегистрирована. {current_quantity} из {total_number}"
    await message.bot.send_message(
        user_telegram_id, context, reply_markup=keyboard_remove()
    )


async def create_participant_game_full(message: Message, command_name: str) -> NoReturn:
    context = f"Итак, вы и ваша команда - {command_name}.\nПоздравляем...\nИ да, название поменять нельзя, сегодня вы {command_name}...\n"
    await message.bot.send_message(
        message.from_user.id, context, reply_markup=keyboard_remove()
    )


async def command_registration_full(
    message: Message, user_telegram_id: int, command_name: str
) -> NoReturn:
    context = f"Команда {command_name}, зарегистрирована. Все команды зарегистрированы, можно начинать игру."
    await message.bot.send_message(
        user_telegram_id, context, reply_markup=await get_inline_keyboard("Старт игры")
    )


async def start_game_participant(message: Message, user_telegram_id: int) -> NoReturn:
    context = f"Для начала игры нажмите старт"
    await message.bot.send_message(
        user_telegram_id, context, reply_markup=await get_inline_keyboard("Старт")
    )
