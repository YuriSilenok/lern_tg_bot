from peewee import CharField, ForeignKeyField
from .table import Table
from .course import Course

class Theme(Table):
    course = ForeignKeyField(model=Course)
    title = CharField()
    url = CharField()
