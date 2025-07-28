"""Модуль содержит функции работы с темой"""

from typing import Any, Dict, List
from models import Course
from models.theme import Theme


def add_theme(course_id: int, title: str, url: str) -> dict:
    """Создает тему для курса"""

    course = Course.get_or_none(id=course_id)
    if course is None:
        raise ValueError(f"Курс с id {course_id} не найден")

    theme, created = Theme.get_or_create(
        course=course,
        title=title,
        url=url,
    )

    if not created:
        raise ValueError(f"Тема '{title}' Вами уже ранее создавалась.")

    return dict(theme)


def get_themes(course_id: int) -> List[Dict[str, Any]]:
    """Вернуть список тем курса"""

    course = Course.get_or_none(id=course_id)
    if course is None:
        raise ValueError(f"Курс с id={course_id} не найден")

    return [
        dict(theme) for theme in Theme.select().where(Theme.course == course)
    ]


def get_theme_by_id(theme_id: int) -> Dict[str, Any]:
    """Получить тему по id"""

    return dict(Theme.get_by_id(theme_id))
