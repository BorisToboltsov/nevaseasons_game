from aiogram.fsm.state import StatesGroup, State


class FSMStartGame(StatesGroup):
    first = State()
    two = State()
