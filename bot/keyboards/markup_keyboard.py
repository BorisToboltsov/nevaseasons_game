from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_markup_main_menu_keyboard(button_list: list) -> types.ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder_list = [
        [builder.add(types.KeyboardButton(text=button)) for button in button_list]
    ]
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)


def get_markup_keyboard(
    button: str, request_contact=False
) -> types.ReplyKeyboardMarkup:
    keyboard = types.KeyboardButton(text=button, request_contact=request_contact)
    markup_keyboard = types.ReplyKeyboardMarkup(
        keyboard=[[keyboard]], resize_keyboard=True
    )
    return markup_keyboard


def keyboard_remove() -> types.ReplyKeyboardRemove:
    return types.ReplyKeyboardRemove()
