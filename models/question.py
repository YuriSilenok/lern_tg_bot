"""Вопрос из теста"""

from peewee import CharField, ForeignKeyField

from .theme import Theme
from .table import Table


class Question(Table):
    """Вопрос по теме"""

    theme = ForeignKeyField(model=Theme)
    text = CharField()

    def __iter__(self):
        yield "id", self.id
        yield "theme", dict(self.theme)
        yield "text", self.text
