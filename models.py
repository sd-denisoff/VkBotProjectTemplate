from peewee import *


db = SqliteDatabase('database.db')


class User(Model):
    vk_id = TextField(primary_key=True)

    class Meta:
        database = db
        db_table = 'Users'
