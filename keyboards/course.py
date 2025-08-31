"""Клавиатуры для курса"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.course import get_courses
from controllers.course import get_all_courses
from filters.permission import IsPermission


def get_my_courses_kb(user_tg_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки c курсами и добавить курс"""

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=course["title"], callback_data=f"course_{course['id']}"
            )
        ]
        for course in get_courses(user_tg_id=user_tg_id)
    ]

    permssion = IsPermission(permission_name="Добавить курс")
    if permssion.check(user_tg_id=user_tg_id):
        inline_keyboard.append(
            [
                InlineKeyboardButton(text="➕", callback_data="add_course"),
            ]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_all_courses_kb() -> InlineKeyboardMarkup:
    """Возвращает кнопки со всеми курсами"""
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=course["title"], callback_data=f"course_{course['id']}"
            )
        ]
        for course in get_all_courses()
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
