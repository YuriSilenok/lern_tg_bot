from datetime import datetime
from peewee import DateTimeField, ForeignKeyField
from .table import Table
from .theme import Theme


class Test(Table):
    theme = ForeignKeyField(model=Theme)
    at_created = DateTimeField(default=datetime.now)
