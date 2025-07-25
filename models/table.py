from peewee import Model
from .connect import db

class Table(Model):

    class Meta:
        database = db
