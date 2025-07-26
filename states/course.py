"""Состояния для действия над курсом"""

from aiogram.fsm.state import StatesGroup, State


class AddCourseState(StatesGroup):
    """Состояния для добавления курса"""

    input_title = State()
