"""Плавиатуры с меню для пользователя"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_keyboard(user_tg_id: int):
    """Получить меню пользователя"""

    keyboard = []
    first_row = []

    first_row.append(KeyboardButton(text="Мои курсы"))

    keyboard.append(first_row)

    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
