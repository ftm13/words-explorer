import peewee
from peewee import MySQLDatabase

db = MySQLDatabase('languageContext', user='root', passwd='fun', host='db')

class MySQLModel(peewee.Model):
    class Meta:
        database = db

class Bigrams(MySQLModel):
    word1 = peewee.CharField()
    word2 = peewee.TextField()
    freq = peewee.IntegerField()

class Sentences(MySQLModel):
    sentence = peewee.TextField()

class Words(MySQLModel):
    word = peewee.CharField()
    freq = peewee.IntegerField()