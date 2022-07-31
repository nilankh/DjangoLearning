from django.db import models
from django.forms import FloatField

# Create your models here.
class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    testScore = FloatField()
    