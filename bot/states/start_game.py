from aiogram.fsm.state import State, StatesGroup


class FSMStartGame(StatesGroup):
    distribution = State()
    choice = State()
    input_text = State()
    input_text_photo = State()
    start = State()
    wait = State()
    end_game = State()
    choice_no_answer = State()
    input_text_no_answer = State()
    input_text_photo_no_answer = State()
    wait_answer = State()
