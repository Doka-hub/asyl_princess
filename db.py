from peewee import (
    MySQLDatabase,
    Model,
    CharField,
    BooleanField,
    IntegerField
)


db = MySQLDatabase(
    'test',
    host='localhost',
    user='root',
    password='123root123',
)


class Person(Model):
    name = CharField()
    is_relative = BooleanField()

    class Meta:
        database = db


if not Person.table_exists():
    Person.create_table()


data = [
    {
        'name': 'Doka',
        'is_relative': True
    },
    {
        'name': 'Albert',
        'is_relative': False
    },
    {
        'name': 'Vova',
        'is_relative': False
    },
]

# for i in data:
#     Person.create(
#         name=i['name'],
#         is_relative=i['is_relative'],
#     )
#
# person_list = Person.select().where(Person.name == 'Albert')
# for person in person_list:
#     person.is_relative = True
#     person.save()

# obj = Person.get(Person.name == 'Doka')
# obj.delete_instance()



"""

1. Создайте модель User с полями:
- username VARCAHAR NOT NULL
- age INT NULL
- user_id INT NOT NULL
2. Создайте 5 разных записей
3. Достаньте те записи, где возраст > 20
"""


class User(Model):
    username = CharField()
    age = IntegerField(null=True)
    user_id = IntegerField()

    class Meta:
        database = db

user_list = User.select().where(User.age > 9)
print(*user_list)
#
# User.create_table()
#
#
# data = [
#     {
#         'username': 'Asyl Princess',
#         'age': 40,
#         'user_id': 100
#     },
#     {
#         'username': 'Doka',
#         'age': 10,
#         'user_id': 101
#     },
# ]
#
#
# for i in data:
#     User.create(
#         username=i['username'],
#         age=i['age'],
#         user_id=i['user_id'],
#     )
