from mongoengine import *
import datetime
connect('mydb')

class Blog(Document):
	title = StringField(required = True, max_length = 100)
	posted = DateTimeField(default = datetime.datetime.now())
	tags = ListField(StringField(max_length=50))
	meta = {'allow_inheritance': True}


class Btest(Blog):
	content = StringField(required =True)


class Ltest(Blog):
	url = StringField(required = True)