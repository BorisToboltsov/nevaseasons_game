from uuid import uuid4


async def link_generation(bot_name: str, quantity: int) -> list:
    link_list = [f'https://t.me/{bot_name}?start_game={uuid4()}' for _ in range(quantity)]
    return link_list
