from peewee import ForeignKeyField
from .table import Table
from .role import Role
from .permission import Permission


class RolePermission(Table):

    role = ForeignKeyField(model=Role)
    permission = ForeignKeyField(model=Permission)
