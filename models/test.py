"""Тест"""

from datetime import datetime
from peewee import DateTimeField, ForeignKeyField
from .table import Table
from .theme import Theme


class Test(Table):
    """Тест"""

    theme = ForeignKeyField(model=Theme)
    at_created = DateTimeField(default=datetime.now)
