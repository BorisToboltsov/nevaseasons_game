from aiogram.types import User
from aiogram_dialog import DialogManager

from database.game.crud.game import DbGame


async def get_game(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    game = DbGame()
    game_list = game.get_all_game(dialog_manager.middleware_data.get('session'))
    return {'game_list': game_list}
