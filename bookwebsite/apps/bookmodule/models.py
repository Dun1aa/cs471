from django.db import models
from django.utils import timezone


# لاب 9: الناشر
class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)


# لاب 9: المؤلف
class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)


class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)

    # حقول اللابات السابقة
    author = models.CharField(max_length=50)
    edition = models.SmallIntegerField(default=1)

    # حقول لاب 9
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField(default=timezone.now)
    rating = models.SmallIntegerField(default=1)

    publisher = models.ForeignKey(
        Publisher,
        null=True,
        on_delete=models.SET_NULL
    )
    authors = models.ManyToManyField(Author)


# لاب 8
class Address(models.Model):
    city = models.CharField(max_length=50)


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE
    )