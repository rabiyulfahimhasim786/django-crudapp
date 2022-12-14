from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Details(models.Model):
    #id=models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=255)
    age=models.IntegerField()
    phone=models.TextField(max_length=255)