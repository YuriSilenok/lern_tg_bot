"""Состояния для действия над темой"""

from aiogram.fsm.state import StatesGroup, State


class AddThemeState(StatesGroup):
    """Состояния для добавления темы"""

    input_title = State()
    input_url = State()
