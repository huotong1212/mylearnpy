from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32,verbose_name="姓名")
    pwd = models.CharField(max_length=32)
    gender = models.IntegerField()
    level = models.IntegerField()
    register_date = models.DateField()