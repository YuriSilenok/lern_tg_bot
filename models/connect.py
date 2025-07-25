"""Подключение к БД"""

from peewee import SqliteDatabase

db = SqliteDatabase(database="sqlite3.db")
