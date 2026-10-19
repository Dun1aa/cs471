from django.db import models
#يعرف بيانات كل كتاب و الاي دي يضيفه الديجانقو تلقائي
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)