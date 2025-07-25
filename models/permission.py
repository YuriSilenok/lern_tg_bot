from peewee import CharField
from .table import Table


class Permission(Table):
    """Привилегия"""

    name = CharField()
