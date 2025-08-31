"""Тест"""

import datetime
from peewee import ForeignKeyField, DateTimeField, IntegerField

from models import course

from .user import User
from .table import Table
from .theme import Theme


class Test(Table):
    """Тест"""

    course = ForeignKeyField(model=course.Course)
    user = ForeignKeyField(model=User)
    at_created = DateTimeField(default=datetime.datetime.now)
    # 0 - не закончен, -1 - провален, 1 - выполнен
    result = IntegerField(default=0)

    def __iter__(self):
        yield "id", self.id
        yield "course", dict(self.course)
        yield "user", dict(self.user)
        yield "at_created", self.at_created
        yield "result", self.result
