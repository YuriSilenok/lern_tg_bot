"""Учебная группа"""

from peewee import CharField
from .table import Table


class Group(Table):
    """Учебная группа"""

    name = CharField()

    def __iter__(self):
        yield "id", self.id
        yield "name", self.name
