"""Модуль содержит функции работы с курсом"""

from typing import Any, Dict, List
from models import Course
from models import User


def add_course(title: str, user_tg_id: int) -> dict:
    """Создает курс для пользователя"""

    course, created = Course.get_or_create(
        owner=User.get_or_none(tg_id=user_tg_id), title=title
    )

    if not created:
        raise ValueError(
            f"Курс с названием '{title}' Вами уже ранее создавался."
        )

    return dict(course)


def get_course_by_id(course_id: int) -> dict:
    """Вернут курс"""

    return dict(Course.get_by_id(pk=course_id))


def get_courses(user_tg_id: int) -> List[Dict[str, Any]]:
    """Вернуть список курсов которые создал пользователь"""

    user = User.get_or_none(tg_id=user_tg_id)
    if user is None:
        raise ValueError(f"Поьзователь с tg_id={user_tg_id} не найден")

    return [
        dict(course) for course in Course.select().where(Course.owner == user)
    ]


def get_all_courses() -> List[Dict[str, Any]]:
    """Вернуть список всех курсов"""
    return [dict(course) for course in Course.select()]
