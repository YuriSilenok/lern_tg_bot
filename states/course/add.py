"""Состояния для добавления курса"""

from aiogram.fsm.state import StatesGroup, State


class AddCourseState(StatesGroup):
    """Состояния для добавления курса"""

    input_course_name = State()
