"""Базовая таблица определяюща идиный коннект для всех моделей"""

from peewee import Model
from .connect import db


class Table(Model):
    """Базовая таблицу"""

    class Meta:
        database = db
