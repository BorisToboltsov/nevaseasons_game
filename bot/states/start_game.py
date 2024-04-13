from aiogram.fsm.state import State, StatesGroup


class FSMStartGame(StatesGroup):
    distribution = State()
    choice = State()
    input_text = State()
    input_text_photo = State()
    start = State()
