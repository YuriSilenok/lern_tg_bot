"""Клавиатуры для тем"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.course import (
    get_subscription,
    user_is_owner,
    user_is_subscription,
)
from controllers.theme import get_theme_by_id, get_themes
from filters.permission import IsPermission


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
