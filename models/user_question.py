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
