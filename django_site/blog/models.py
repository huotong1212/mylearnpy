from django.db import models

# Create your models here.
class Book(models.Model):  #必须要继承的
    nid = models.AutoField(primary_key=True)  #自增id(可以不写，默认会有自增id)
    title = models.CharField(max_length=32)
    publishDdata = models.DateField()  #出版日期
    author = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5,decimal_places=2)  #一共5位，保留两位小数

class Auther(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    age = models.IntegerField()


