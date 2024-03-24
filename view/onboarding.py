from aiogram.types import Message

from bot.keyboards.markup_keyboard import get_markup_keyboard, keyboard_remove


async def send_phone(message: Message):
    context = "Чтобы идентифицировать вас, нам необходим ваш номер телефона. Нажмите на кнопку ниже."
    await message.bot.send_message(message.from_user.id, context, reply_markup=get_markup_keyboard('Отправить номер телефона', True))


async def not_register(message: Message):
    context = "Вы не зарегистрированы. Обратитесь в ОРП."
    await message.bot.send_message(message.from_user.id, context, reply_markup=keyboard_remove())


async def connect_success(message: Message):
    context = "Поздравляем вы подключены к игре в качестве ведущего."
    await message.bot.send_message(message.from_user.id, context, reply_markup=keyboard_remove())


async def game_is_finished(message: Message):
    context = "Игра закончена!"
    await message.bot.send_message(message.from_user.id, context, reply_markup=keyboard_remove())


async def invalid_link(message: Message):
    context = "Не верная ссылка. Нужно чтобы ведущий создал игру."
    await message.bot.send_message(message.from_user.id, context, reply_markup=keyboard_remove())
