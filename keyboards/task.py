"""Клавиатура для задач"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.task import get_tasks


def get_tasks_kb(theme_id: int) -> InlineKeyboardMarkup:
    """Вернёт список кнопок с задачами для укзанной темы"""

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=task["title"], callback_data=f"test_{task['id']}"
            )
        ]
        for task in get_tasks(theme_id=theme_id)
    ]
    inline_keyboard.append(
        [
            InlineKeyboardButton(
                text="⏪",
                callback_data=f"theme_{theme_id}",
            ),
            InlineKeyboardButton(
                text="➕", callback_data=f"add_task_{theme_id}"
            ),
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
