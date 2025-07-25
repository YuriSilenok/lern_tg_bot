"""Модуль содержит функции работы с курсом"""

from typing import Any, Dict, List
from models import Course
from models.user import User


def add_course(name: str, user_tg_id: int) -> dict:
    """Создает курс для пользователя"""

    course, created = Course.get_or_create(
        owner=User.get_or_none(tg_id=user_tg_id), name=name
    )

    if not created:
        raise ValueError(
            f"Курс с названием '{name}' Вами уже ранее создавался."
        )

    return dict(course)


def get_courses(user_tg_id: int) -> List[Dict[str, Any]]:
    """Вернуть список курсов которые создал пользователь"""

    user = User.get_or_none(tg_id=user_tg_id)

    return [
        dict(course) for course in Course.select().where(Course.owner == user)
    ]
