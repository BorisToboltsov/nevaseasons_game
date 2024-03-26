from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.text import Const

from bot.states.start_game import FSMStartGame

start_game_dialog = Dialog(
    Window(
        Const(text='Можно начинать новую игру!'),
        state=FSMStartGame.first
    ),
)
