"""Клавиатуры для курсов"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from models.course import Course
from models.user import User


def get_kb(user_tg_id: int) -> InlineKeyboardMarkup:

    user = User.get_or_none(tg_id=user_tg_id)

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=course.name, callback_data=f"course_{course.id}"
            )
        ]
        for course in Course.select().where(Course.owner == user)
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
