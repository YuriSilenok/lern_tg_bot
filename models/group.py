from peewee import CharField
from .table import Table


class Group(Table):

    name = CharField()
