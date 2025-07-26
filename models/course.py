"""Учебный курс"""

# pylint: disable=E1101

from peewee import CharField, ForeignKeyField
from .table import Table
from .user import User


class Course(Table):
    """Учебный курс"""

    owner = ForeignKeyField(model=User)
    title = CharField()

    def __iter__(self):
        yield "id", self.id
        yield "title", self.title
        yield "owner", dict(self.owner)
