"""Плавиатуры с меню для пользователя"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from filters.permission import IsPermission


PERMISSION_BUTTON = [
    ("Просмотр групп", "Мои группы"),
    ("Просмотр всех курсов", "Все курсы"),
]


def get_menu_kb(user_tg_id: int) -> ReplyKeyboardMarkup:
    """Получить меню пользователя"""

    keyboard = []
    first_row = []

    first_row.append(KeyboardButton(text="Мои курсы"))

    for permission_name, text in PERMISSION_BUTTON:
        permssion = IsPermission(permission_name=permission_name)
        if permssion.check(user_tg_id=user_tg_id):
            first_row.append(KeyboardButton(text=text))

    keyboard.append(first_row)

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
