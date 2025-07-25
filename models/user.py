from peewee import CharField, IntegerField
from .table import Table


class User(Table):
    """Ответ"""

    tg_id = IntegerField()
    username = CharField(null=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    fio = CharField(null=True)

    def __iter__(self):
        yield "tg_id", self.tg_id
        yield "username", self.username
        yield "first_name", self.first_name
        yield "last_name", self.last_name
        yield "fio", self.fio
