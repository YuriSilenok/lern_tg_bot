"""Логика для ответов"""

from typing import Any, Dict, List

from models.answer import Answer
from models.question import Question


def get_answers(question_id: int) -> List[Dict[str, Any]]:
    """Вернуть список курсов которые создал пользователь"""

    question = Question.get_or_none(id=question_id)
    if question is None:
        raise ValueError(f"Вопрос с id={question_id} не найден")

    return [
        dict(answer)
        for answer in Answer.select().where(Answer.question == question)
    ]


def add_answer(
    question_id: int, text: str, is_valid: bool = False
) -> Dict[str, Any]:
    """Добавляет вариант ответа вопросу"""

    answer, created = Answer.get_or_create(
        question=Question.get(id=question_id), text=text, is_valid=is_valid
    )

    if not created:
        raise ValueError(
            f"Вариант ответа с текстом '{text}' Вами уже ранее создавался."
        )

    return dict(answer)


def set_answer(
    answer_id: int, text: str = None, is_valid: bool = None
) -> Dict[str, Any]:
    """Обновляет атрибуты объекта"""

    answer: Answer = Answer.get_or_none(id=answer_id)
    if answer is None:
        raise ValueError(f"Вариант ответа с id={answer_id} не найден")

    if text:
        answer.text = text

    if is_valid is not None:
        answer.is_valid = is_valid

    answer.save()

    return dict(answer)


def get_answer_by_id(answer_id: int) -> Dict[str, Any]:
    """Подучить вариант ответа по ИД"""

    answer: Answer = Answer.get_or_none(id=answer_id)
    if answer is None:
        raise ValueError(f"Вариант ответа с id={answer_id} не найден")

    return dict(answer)
