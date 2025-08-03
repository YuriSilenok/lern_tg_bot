"""Логика для вопросов"""

from typing import Any, Dict, List
from models.question import Question
from models.theme import Theme


def add_question(theme_id: int, text: str) -> dict:
    """Создает вопрос"""

    question, created = Question.get_or_create(
        theme=Theme.get(id=theme_id), text=text
    )

    if not created:
        raise ValueError(
            f"Вопрос с текстом '{text}' Вами уже ранее создавался."
        )

    return dict(question)


def get_questions(theme_id: int) -> List[Dict[str, Any]]:
    """Получает список вопросов для темы"""

    theme = Theme.get_or_none(id=theme_id)
    if theme is None:
        raise ValueError(f"Темы с id={theme_id} не найдено")

    return [
        dict(question)
        for question in Question.select().where(Question.theme == theme)
    ]


def get_question_by_id(question_id: int) -> Dict[str, Any]:
    """Получить вопрос по ид"""

    return dict(Question.get_by_id(question_id))
