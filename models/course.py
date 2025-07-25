"""Учебный курс"""

from peewee import CharField, ForeignKeyField
from .table import Table
from .user import User


class Course(Table):
    """Учебный курс"""

    owner = ForeignKeyField(model=User)
    name = CharField()

    def __iter__(self):
        yield "name", self.name
        yield "owner", dict(self.owner)
