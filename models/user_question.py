"""Статистика ответов на вопросы пользователем"""

from peewee import ForeignKeyField, IntegerField

from .question import Question
from .table import Table
from .user import User


class UserQuestion(Table):
    """Вопросы на которые отвечал пользователь"""

    user = ForeignKeyField(model=User)
    question = ForeignKeyField(model=Question)
    score = IntegerField(default=0)

    def __iter__(self):
        yield "id", self.id
        yield "user", dict(self.user)
        yield "question", dict(self.question)
        yield "score", self.score
