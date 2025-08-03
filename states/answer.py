"""Состояния для действия с вариантом ответа"""

from aiogram.fsm.state import StatesGroup, State


class AddAnswerState(StatesGroup):
    """Состояния для добавления варианта ответа"""

    input_text = State()
