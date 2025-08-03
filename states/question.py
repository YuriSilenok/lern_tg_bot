"""Состояния для действия с вопросом"""

from aiogram.fsm.state import StatesGroup, State


class AddQuestionState(StatesGroup):
    """Состояния для добавления вопроса"""

    input_text = State()
