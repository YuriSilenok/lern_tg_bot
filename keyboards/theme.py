"""Клавиатуры для тем"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.theme import get_theme_by_id, get_themes


def get_theme_kb(theme_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки для выбранной темы"""

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
                text="⏪", callback_data="courses"
            ),
            InlineKeyboardButton(
                text="➕", callback_data=f"add_theme_{course_id}"
            ),
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
