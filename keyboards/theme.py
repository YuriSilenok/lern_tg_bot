"""Клавиатуры для тем"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.theme import get_themes


def get_theme_kb(theme_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки для выбранной темы"""

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text="Тесты", callback_data=f"tests_theme_{theme_id}"
            ),
            InlineKeyboardButton(
                text="Задачи", callback_data=f"tasks_theme_{theme_id}"
            ),
        ]
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_themes_kb_by_teacher(course_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки c темами курса для преподавателя"""

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
