from django.db import models

class family(models.Model):
    name=models.CharField(max_length=20)
