"""Модуль подписки на курс"""

from peewee import ForeignKeyField

from models.course import Course
from models.user import User
from .table import Table


class Subscription(Table):
    """Подписка на курс"""

    user = ForeignKeyField(model=User)
    course = ForeignKeyField(model=Course)

    def __iter__(self):
        yield "id", self.id
        yield "user", dict(self.user)
        yield "course", dict(self.course)
