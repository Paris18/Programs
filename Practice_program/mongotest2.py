from mongoengine import *
connect('mydb')

post = Btest(title = "test1", content = "hi")
post.save()