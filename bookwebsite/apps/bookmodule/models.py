from django.db import models
#يعرف بيانات كل كتاب و الاي دي يضيفه الديجانقو تلقائي
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)


#-----------------لاب8 ستيب 6
class Address(models.Model):#يحفظ اسم المدينه
    city = models.CharField(max_length=50)


class Student(models.Model):#يحفظ اسم الطالب وعمره
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )