from aiogram import types


async def get_inline_keyboard(*args: str) -> types.InlineKeyboardMarkup:
    button = [
        [types.InlineKeyboardButton(text=name, callback_data=name) for name in args]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard
