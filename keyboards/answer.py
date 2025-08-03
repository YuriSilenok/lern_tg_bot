"""Клавиатуры для варианта ответа"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.answer import get_answer_by_id, get_answers


def get_answer_kb(answer_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки  для варианта ответа"""

    answer = get_answer_by_id(answer_id=answer_id)
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text="⏪", callback_data=f"question_{answer['question']['id']}"
            ),
            InlineKeyboardButton(
                text="✅Верный", callback_data=f"answer_yes_{answer_id}"
            ),
            InlineKeyboardButton(
                text="❌Неверный", callback_data=f"answer_no_{answer_id}"
            ),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
