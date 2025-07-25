from peewee import CharField, ForeignKeyField
from .table import Table
from .test import Test


class Question(Table):
    """Вопрос"""

    test = ForeignKeyField(model=Test)
    text = CharField()
