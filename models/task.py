"""Модель задачи"""

from peewee import ForeignKeyField, CharField
from .table import Table
from .theme import Theme


class Task(Table):
    """Задача"""

    theme = ForeignKeyField(model=Theme)
    title = CharField()

    def __iter__(self):
        yield "id", self.id
        yield "theme", dict(self.theme)
        yield "title", self.title
