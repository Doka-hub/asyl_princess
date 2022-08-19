"""
1. Создайте новый проект
2. Создайте файлы:
 - db.py
 - models.py
 - config.py
3. Создайте репозиторий db_practice
4. Добавьте в репозиторий все файлы
5. Подключите mysql базу данных в файле db с помощью peewee
6. Создайте модели в файле models.py:
- TGUser (
tg_user_id INT NOT NULL,
username VARCHAR NULL,
)
- Note (
user_id INT NOT NULL FOREIGN KEY (TGUser),
note TEXT NOT NULL,
date DATE,
)


"""

from peewee import (
    MySQLDatabase,
    Model,
    CharField,
    IntegerField,
    TextField,
    DateField,
    ForeignKeyField,
)

db = MySQLDatabase(
    'db_practice',
    host='localhost',
    user='root',
    password='Zsynth91!'
)


class TGUser(Model):
    tg_user_id = IntegerField()
    username = CharField(null=True)

    class Meta:
        database = db


class Note(Model):
    user_id = ForeignKeyField(TGUser, on_delete='CASCADE')
    note = TextField()
    date = DateField()

    class Meta:
        database = db


if not TGUser.table_exists():
    TGUser.create_table()

if not Note.table_exists():
    Note.create_table()
