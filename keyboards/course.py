"""Клавиатуры для курса"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.course import get_courses_by_owner, get_subscription
from controllers.course import get_all_courses
from filters.permission import IsPermission


def get_my_courses_kb(user_tg_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки для пункта меню Мои курсы"""

    courses = get_courses_by_owner(user_tg_id=user_tg_id)
    
    # дополняем подписками на курс но без дубликатов
    for course in get_subscription(user_tg_id=user_tg_id):
        if len(filter(lambda c: c['id'] == course['id'], courses)) == 0:
            courses.append(course)
    

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=course["title"], callback_data=f"course_{course['id']}"
            )
        ]
        for course in courses
    ]

    # если есть роль преподавателя, то доступна кнопка Добавить курс
    permssion = IsPermission(permission_name="Добавить курс")
    if permssion.check(user_tg_id=user_tg_id):
        inline_keyboard.append(
            [
                InlineKeyboardButton(text="➕", callback_data="add_course"),
            ]
        )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


def get_all_courses_kb() -> InlineKeyboardMarkup:
    """Возвращает кнопки для пункта меню Все курсы"""
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=course["title"], callback_data=f"course_{course['id']}"
            )
        ]
        for course in get_all_courses()
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
