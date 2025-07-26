"""Тема"""

from peewee import CharField, ForeignKeyField
from .table import Table
from .course import Course


class Theme(Table):
    """Тема"""

    course = ForeignKeyField(model=Course)
    title = CharField()
    url = CharField()

    def __iter__(self):
        yield "id", self.id
        yield "course", dict(self.course),
        yield "title", self.title
        yield "url", self.url
