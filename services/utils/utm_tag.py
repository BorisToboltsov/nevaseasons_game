from typing import NoReturn

from aiogram.types import Message


class UtmTag:
    def __init__(self):
        self.utm_tag = ""

    async def parse_utm_tag(self, message: Message) -> NoReturn:
        try:
            utm_tag = message.text.split(" ")[1]
            if len(utm_tag) > 100:
                utm_tag = None
        except IndexError:
            utm_tag = None
        self.utm_tag = utm_tag
