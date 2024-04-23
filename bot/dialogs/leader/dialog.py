from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const, Format

from bot.dialogs.leader.getters import get_text
from bot.dialogs.leader.handlers import button_no, button_yes
from bot.states.leader import FSMLeader

leader_dialog = Dialog(
    Window(
        Format(
            "Команда {command_name}:\nОтвет команды {participant_answer}\nПравильный ответ{correct_answer}"
        ),
        Button(text=Const("Да"), id="yes", on_click=button_yes),
        Button(text=Const("Нет"), id="no", on_click=button_no),
        state=FSMLeader.first,
        getter=get_text,
    ),
)
