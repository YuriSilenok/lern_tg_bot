"""Вариант ответа в тесте для вопроса"""

from peewee import CharField, BooleanField, ForeignKeyField
from .table import Table
from .question import Question


class Answer(Table):
    """Вариант ответа для вопроса"""

    question = ForeignKeyField(model=Question)
    text = CharField()
    is_valid = BooleanField(default=False)


    def __iter__(self):
        yield "id", self.id
        yield "question", dict(self.question)
        yield "text", self.text
        yield "is_valid", self.is_valid
