import os
from typing import NoReturn

from aiogram.types import FSInputFile, Message

from database.customer import DbCustomer
from services.utils.return_name import return_name
from services.utm.utm_tag import UtmTag
from view.onboarding.onboarding import (
    customer_exist,
    link_site,
    welcome_onboarding_message, account_is_blocked,
)


class Start:
    @staticmethod
    async def start(message: Message) -> NoReturn:
        customer = DbCustomer()
        customer = await customer.get_customer_by_telegram_id(message.from_user.id)
        if customer.get("success") is False and customer.get('messages') == ['Учетная запись пользователя заблокирована!']:
            await account_is_blocked(message.from_user.id)
        elif customer.get("success") is False or customer.get('data').get('status_mnemo') == 'UNCONFIRMED':
            photo = FSInputFile(f"{os.getenv('PATH_IMAGE')}how_open_keyboard.png")
            await welcome_onboarding_message(message.from_user.id, photo)
        else:
            utm_tag = UtmTag()
            await utm_tag.parse_utm_tag(message)

            if utm_tag.utm_tag == "authorization":
                await link_site(message.from_user.id, customer["data"]["auth_token"])
            else:
                name = await return_name(customer)
                photo = FSInputFile(f"{os.getenv('PATH_IMAGE')}how_open_keyboard.png")
                await customer_exist(message.from_user.id, name, photo)
