"""Роль"""

from peewee import CharField
from .table import Table


class Role(Table):
    """Роль"""

    name = CharField()
