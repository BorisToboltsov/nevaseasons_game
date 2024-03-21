from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def get_inline_keyboard(*args: str) -> types.InlineKeyboardMarkup:
    button = [
        [types.InlineKeyboardButton(text=name, callback_data=name) for name in args]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


async def get_feedback_inline_keyboard(token: str) -> types.InlineKeyboardMarkup:
    button = [
        [
            types.InlineKeyboardButton(
                text="Создать обращение",
                url=f"https://sp-zp.ru/cabinet/messages/?token={token}",
            )
        ],
        [types.InlineKeyboardButton(text="Позвонить!", callback_data="Позвонить!")],
        [
            types.InlineKeyboardButton(
                text="Заказать звонок", callback_data="Заказать звонок"
            )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


async def get_payment_fee_inline_keyboard(
    token: str, order: str
) -> types.InlineKeyboardMarkup:
    button = [
        [
            types.InlineKeyboardButton(
                text="Оплачу позже", callback_data="Оплачу позже"
            ),
            types.InlineKeyboardButton(
                text="Оплатить на сайте",
                url=f"https://sp-zp.ru/cabinet/order?id={order}&token={token}",
            ),
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


async def get_link_site_inline_keyboard(token: str) -> types.InlineKeyboardMarkup:
    button = [
        [
            types.InlineKeyboardButton(
                text="Вход в ЛК", url=f"https://sp-zp.ru/cabinet/?token={token}"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Билеты", url=f"https://sp-zp.ru/theaters/?token={token}"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="️Экскурсии", url=f"https://sp-zp.ru/excursions/?token={token}"
            )
        ],
        [
            types.InlineKeyboardButton(
                text="Спорт", url=f"https://sp-zp.ru/uslugi/?token={token}"
            )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


async def get_telegram_channel_inline_keyboard() -> types.InlineKeyboardMarkup:
    button = [
        [types.InlineKeyboardButton(text="Перейти!", url=f"https://t.me/ZolotaiPora")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard


async def get_my_order_inline_keyboard(
    order_id: str, token: str, button_name: str
) -> types.InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder_list = [
        [
            builder.add(
                types.InlineKeyboardButton(
                    text=f"{button_name}",
                    url=f"https://sp-zp.ru/cabinet/order?id={order_id}&token={token}",
                )
            )
        ],
    ]
    builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)


async def get_create_request_keyboard(token: str) -> types.InlineKeyboardMarkup:
    button = [
        [
            types.InlineKeyboardButton(
                text="Создать обращение",
                url=f"https://sp-zp.ru/cabinet/messages/?token={token}",
            )
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=button)
    return keyboard
