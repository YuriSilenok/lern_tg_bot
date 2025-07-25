from peewee import ForeignKeyField
from .table import Table
from .user import User
from .role import Role


class UserRole(Table):

    user = ForeignKeyField(model=User)
    role = ForeignKeyField(model=Role)
