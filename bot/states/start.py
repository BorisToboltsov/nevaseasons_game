from aiogram.fsm.state import StatesGroup, State


class FSMStartGame(StatesGroup):
    start = State()
