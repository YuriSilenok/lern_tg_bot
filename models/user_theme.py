"""Хранит сведения об освоенных темах"""

from peewee import ForeignKeyField

from models.table import Table
from models.theme import Theme
from models.user import User


class UserTheme(Table):
    """Освоенные темы"""

    user = ForeignKeyField(model=User)
    theme = ForeignKeyField(model=Theme)
