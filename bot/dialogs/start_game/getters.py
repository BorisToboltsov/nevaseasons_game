from aiogram.enums import ContentType
from aiogram.types import User
from aiogram_dialog import DialogManager
from aiogram_dialog.api.entities import MediaAttachment

from database.game.crud.game import DbGame


async def get_game(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    game = DbGame()
    game_list = game.get_all_game(dialog_manager.middleware_data.get('session'))
    return {'game_list': game_list}


async def get_command_quantity(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    return {'command_quantity': dialog_manager.dialog_data['command_quantity']}


async def get_data(**kwargs):
    dialog_manager = kwargs.get('dialog_manager')
    qr_code_path_list = dialog_manager.dialog_data['qr_code_path_list']
    try:
        number_list = dialog_manager.dialog_data['number_list_go_next']
    except KeyError:
        number_list = 0
        dialog_manager.dialog_data['number_list_go_next'] = number_list
    qr_code_path = qr_code_path_list[number_list]
    image = MediaAttachment(ContentType.PHOTO, path=qr_code_path)

    return {'photo': image, 'text': number_list + 1}
