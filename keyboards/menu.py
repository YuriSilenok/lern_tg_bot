"""Плавиатуры с меню для пользователя"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from filters.permission import IsPermission


def get_menu_kb(user_tg_id: int) -> ReplyKeyboardMarkup:
    """Получить меню пользователя"""

    keyboard = []
    first_row = []

    first_row.append(KeyboardButton(text="Мои курсы"))

    teacher_permition = IsPermission(permission_name="Просмотр групп")
    if teacher_permition.check(user_tg_id=user_tg_id):
        first_row.append(KeyboardButton(text="Мои группы"))

    keyboard.append(first_row)

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
