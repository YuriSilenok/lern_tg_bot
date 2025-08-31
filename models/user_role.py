"""Роли пользователя"""

from peewee import ForeignKeyField
from .table import Table
from .user import User
from .role import Role


class UserRole(Table):
    """Выданные роли пользователю"""

    user = ForeignKeyField(model=User)
    role = ForeignKeyField(model=Role)

    def __iter__(self):
        yield "id", self.id
        yield "user", dict(self.user)
        yield "role", dict(self.role)
