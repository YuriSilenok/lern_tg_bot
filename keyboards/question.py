"""Клавиатуры для курса"""

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from controllers.answer import get_answers
from controllers.course import get_courses
from controllers.question import get_question_by_id, get_questions


def get_question_kb(question_id: int) -> InlineKeyboardMarkup:
    """Возвращает кнопки для вопроса"""

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=f"{'✅' if answer['is_valid'] else '❌'} {answer['text']}",
                callback_data=f"answer_{answer['id']}"
            )
        ]
        for answer in get_answers(question_id=question_id)
    ]


    question = get_question_by_id(question_id=question_id)
    inline_keyboard.append(
        [
            InlineKeyboardButton(
                text="⏪",
                callback_data=f"questions_theme_{question['theme']['id']}"
            ),
            InlineKeyboardButton(
                text="➕",
                callback_data=f"add_answer_{question_id}"
            ),
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

def get_questions_kb(theme_id: int) -> InlineKeyboardMarkup:
    """Получает список вопросов для темы в виде кнопок"""

    inline_keyboard = [
        [
            InlineKeyboardButton(
                text=question["text"], callback_data=f"question_{question['id']}"
            )
        ]
        for question in get_questions(theme_id=theme_id)
    ]

    inline_keyboard.append(
        [
            InlineKeyboardButton(
                text="⏪", callback_data=f"theme_{theme_id}"
            ),
            InlineKeyboardButton(
                text="➕", callback_data=f"add_question_{theme_id}"
            )
        ]
    )

    return InlineKeyboardMarkup(inline_keyboard=inline_keyboard)