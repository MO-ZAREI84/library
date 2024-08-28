from django.db import models
from datetime import datetime

class BookManager(models.Manager):
    def archived_excluded_queryset(self):
        return self.filter(archived=False)

class Author(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=20)
    authors = models.ManyToManyField(Author)
    archived = models.BooleanField(default=False)
    publication_date = models.DateTimeField(default=datetime.fromisoformat("2023-08-28T10:45:00"))
    pages_count = models.IntegerField(default=12)
    price=models.IntegerField(default ='13333')

class Profile(models.Model):
    email = models.EmailField(default='default@example.com')
    phone_number = models.IntegerField()

class Person(models.Model):
    Gender_Choices = [
        ('f', 'female'),
        ('m', 'male'),
    ]
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=Gender_Choices, default='m')

class Library(models.Model):
    number = models.CharField(max_length=12)
