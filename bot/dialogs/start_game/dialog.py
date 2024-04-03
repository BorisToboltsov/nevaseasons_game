from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.start_game.getters import get_task
from bot.states.start_game import FSMStartGame

start_game_dialog = Dialog(
    Window(
        Format('Команда №{text}'),
        # Const('Тест'),
        state=FSMStartGame.first,
        getter=get_task,
    ),
)
