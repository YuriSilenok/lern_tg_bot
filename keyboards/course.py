"""Клавиатуры для курсов"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.course import get_courses


def get_kb(user_tg_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки c курсами и добавить курс"""

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=course["title"], callback_data=f"course_{course['id']}"
            )
        ]
        for course in get_courses(user_tg_id=user_tg_id)
    ]

    inline_keyboard.append(
        [
            InlineKeyboardButton(
                text="Добавить курс", callback_data="add_course"
            )
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
