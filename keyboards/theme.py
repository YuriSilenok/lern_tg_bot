"""Клавиатуры для тем"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.theme import get_theme_by_id


def get_theme_kb(theme_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки для пункта меню Тема курса"""

    theme = get_theme_by_id(theme_id=theme_id)
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text="⏪", callback_data=f"course_{theme['course']['id']}"
            ),
            InlineKeyboardButton(
                text="❓Вопросы", callback_data=f"questions_theme_{theme_id}"
            ),
            InlineKeyboardButton(
                text="📝Задачи", callback_data=f"tasks_theme_{theme_id}"
            ),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
