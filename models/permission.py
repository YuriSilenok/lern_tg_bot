"""Привилегии пользователей"""

from peewee import CharField
from .table import Table


class Permission(Table):
    """Привилегия"""

    name = CharField()

    def __iter__(self):
        yield "id", self.id
        yield "name", self.name
