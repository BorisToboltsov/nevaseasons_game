from aiogram.fsm.state import State, StatesGroup


class FSMOnboarding(StatesGroup):
    first = State()
    two = State()
    three = State()
    four = State()
    five = State()
