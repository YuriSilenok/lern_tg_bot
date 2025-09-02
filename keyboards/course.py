"""Клавиатуры для курса"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.course import (
    get_courses_by_owner,
    get_subscription,
    user_is_owner,
)
from controllers.course import get_all_courses
from controllers.theme import get_themes
from filters.permission import IsPermission


def get_my_courses_kb(user_tg_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки для пункта меню Мои курсы"""

    courses = get_courses_by_owner(user_tg_id=user_tg_id)

    # дополняем подписками на курс но без дубликатов
    for course in get_subscription(user_tg_id=user_tg_id):
        if len(filter(lambda c: c["id"] == course["id"], courses)) == 0:
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


def get_themes_kb(course_id: int, user_tg_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки для пункта меню Темы курса"""

    # Список тем
    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=theme["title"], callback_data=f"theme_{theme['id']}"
            )
        ]
        for theme in get_themes(course_id=course_id)
    ]

    last_row = [InlineKeyboardButton(text="⏪", callback_data="courses")]

    # Если у пользователя есть привелегия добавлять тему и он автор курса
    is_permission = IsPermission(permission_name="Добавить тему").check(
        user_tg_id=user_tg_id
    )
    is_owner = user_is_owner(course_id=course_id, user_tg_id=user_tg_id)
    if is_permission and is_owner:
        last_row.append(
            InlineKeyboardButton(
                text="➕", callback_data=f"add_theme_{course_id}"
            )
        )

    # Проверяем наличие подписки на курс
    subscription = get_subscription(course_id=course_id, user_tg_id=user_tg_id)
    if subscription:
        last_row.append(
            InlineKeyboardButton(
                text="🔕",
                callback_data=f"unsubscribe_{subscription['id']}",
            )
        )
    else:
        last_row.append(
            InlineKeyboardButton(
                text="🔔",
                callback_data=f"subscribe_{course_id}",
            )
        )

    inline_keyboard.append(last_row)

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
