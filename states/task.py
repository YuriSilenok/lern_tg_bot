"""Действия над задачей"""

from aiogram.fsm.state import StatesGroup, State


class AddTaskState(StatesGroup):
    """Состояния для добавления задачи"""

    input_title = State()
    input_url = State()
