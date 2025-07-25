from peewee import CharField, BooleanField, ForeignKeyField
from .table import Table
from .question import Question


class Answer(Table):
    """Ответ"""

    question = ForeignKeyField(model=Question)
    text = CharField()
    is_valid = BooleanField()
