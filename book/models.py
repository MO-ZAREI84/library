from django.db import models

class Author (models.Model):
    name=models.CharField(max_length=10)

class Book(models.Model):
    title=models.CharField(max_length=20)
    authors=models.ManyToManyField(Author)
    
class Profile(models.Model):
    email=models.EmailField()
    phone_number=models.IntegerField()

class Personal(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
