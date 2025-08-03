"""Клавиатура для тестов"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.test import get_tests


def get_tests_kb(theme_id: int):
    """Вернёт список кнопок с тестами для укзанной темы"""

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=test["title"], callback_data=f"test_{test['id']}"
            )
        ]
        for test in get_tests(theme_id=theme_id)
    ]

    inline_keyboard.append(
        [
            InlineKeyboardButton(
                text="Добавить тест", callback_data=f"add_test_{theme_id}"
            )
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
