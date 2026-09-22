from django.db import models

# Create your models here.
#orm - object relational mapping

class Students(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

