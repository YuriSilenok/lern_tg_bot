from peewee import CharField, ForeignKeyField
from .table import Table
from .course import Course


class Group(Table):

    name = CharField()
