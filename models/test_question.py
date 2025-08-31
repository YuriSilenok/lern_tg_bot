"""Вопросы теста"""

from peewee import ForeignKeyField, IntegerField

from models.question import Question
from models.test import Test

from .table import Table


class TestQuestion(Table):
    """Ответ на вопрос"""

    test = ForeignKeyField(model=Test)
    question = ForeignKeyField(model=Question)
    answer = IntegerField(default=0)  # 0 - не отвечал, 1 - верно, -1 ошибка

    def __iter__(self):
        yield "id", self.id
        yield "test", dict(self.test)
        yield "question", dict(self.question)
        yield "answer", self.answer
