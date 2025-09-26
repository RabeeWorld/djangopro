from django.db import models


# Create your models here.

class Student(models.Model):
    Name=models.CharField(max_length=20)
    Roll_no=models.IntegerField(primary_key=True)
    Address=models.TextField()
    Mobile_no=models.BigIntegerField()