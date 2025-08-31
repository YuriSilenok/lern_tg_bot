"""Роль"""

from peewee import CharField
from .table import Table


class Role(Table):
    """Роль"""

    name = CharField()

    def __iter__(self):
        yield "id", self.id
        yield "name", self.name
