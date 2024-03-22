from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from bot.states.start import FSMStartGame

start_game_dialog = Dialog(
    Window(
        Const(text='Это просто текст'),
        state=FSMStartGame.start
    ),
)
