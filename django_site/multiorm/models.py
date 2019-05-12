from django.db import models

# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=20,verbose_name="名字")
    price=models.IntegerField()
    cost = models.IntegerField(default=100)
    pub_date=models.DateField()
    publish=models.ForeignKey("Publish",on_delete=models.CASCADE) # 外键默认关联主键 publish_id
    authors=models.ManyToManyField("Author")


    def __str__(self):
        return self.name

class Publish(models.Model):

    name=models.CharField(max_length=32)
    city=models.CharField(max_length=32)

    def __str__(self):
        return self.name


# class Book_Author(models.Model):
#     book=models.ForeignKey("Book")
#     author=models.ForeignKey("Author")


class Author(models.Model):

    name=models.CharField(max_length=32)
    age=models.IntegerField(default=20)

    def __str__(self):
        return self.name
