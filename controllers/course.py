"""Модуль содержит функции работы с курсом"""

from typing import Any, Dict, List, Union
from models import Course
from models import User
from models.subscription import Subscription


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


def get_courses_by_owner(user_tg_id: int) -> List[Dict[str, Any]]:
    """Вернуть список курсов которые создал пользователь"""

    user = User.get_or_none(tg_id=user_tg_id)

    return [
        dict(course) for course in Course.select().where(Course.owner == user)
    ]


def get_subscription(user_tg_id: int) -> List[Dict]:
    """Вернуть список курсов на которые подписался пользователь"""
    return [dict(sub.course) for sub in Subscription.select().where(Subscription.user == User.get(tg_id=user_tg_id))]


def get_all_courses() -> List[Dict[str, Any]]:
    """Вернуть список всех курсов"""
    return [dict(course) for course in Course.select()]


def user_is_owner(course_id: int, user_tg_id: int) ->bool:
    """Проверяет, является ли пользователь автором курса"""
    return Course.get_or_none(id=course_id, owner=User.get(tg_id=user_tg_id)) is not None


def get_subscription(course_id: int, user_tg_id: int) -> Union[Dict[str, Any], None]:
    """Получает подписку по курсу для пользователя"""

    return Subscription.get_or_none(course=course_id, user=User.get(tg_id=user_tg_id))


def user_is_subscription(course_id: int, user_tg_id: int) -> bool:
    """Проверяет подписку пользователя на курс"""

    return get_subscription(course_id=course_id, user_tg_id=user_tg_id) is not None