"""Клавиатуры для тем"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.theme import get_themes


def get_kb(course_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки c темами и добавить тему"""

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=theme["title"], callback_data=f"theme_{theme['id']}"
            )
        ]
        for theme in get_themes(course_id=course_id)
    ]

    inline_keyboard.append(
        [
            InlineKeyboardButton(
                text="Добавить тему", callback_data=f"add_theme_{course_id}"
            )
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
