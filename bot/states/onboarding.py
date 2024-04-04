from aiogram.fsm.state import StatesGroup, State


class FSMOnboarding(StatesGroup):
    first = State()
    two = State()
    three = State()
    four = State()
    five = State()
