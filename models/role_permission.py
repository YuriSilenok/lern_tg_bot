"""Выданные привилегии роли"""

from peewee import ForeignKeyField
from .table import Table
from .role import Role
from .permission import Permission


class RolePermission(Table):
    """Выданные привилегии роли"""

    role = ForeignKeyField(model=Role)
    permission = ForeignKeyField(model=Permission)
