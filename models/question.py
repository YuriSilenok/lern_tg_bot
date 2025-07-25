"""Вопрос из теста"""

from peewee import CharField, ForeignKeyField
from .table import Table
from .test import Test


class Question(Table):
    """Вопрос из теста"""

    test = ForeignKeyField(model=Test)
    text = CharField()
