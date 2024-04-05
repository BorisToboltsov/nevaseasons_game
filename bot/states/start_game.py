from aiogram.fsm.state import StatesGroup, State


class FSMStartGame(StatesGroup):
    distribution = State()
    choice = State()
    input_text = State()
    input_text_photo = State()
    test = State()
