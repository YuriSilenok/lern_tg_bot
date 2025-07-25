"""Учебная группа"""

from peewee import CharField
from .table import Table


class Group(Table):
    """Учебная группа"""

    name = CharField()
