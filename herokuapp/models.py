from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/2.2/ref/models/fields/
# https://docs.djangoproject.com/en/2.2/topics/db/sql/


class User(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    cmnd = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    born = models.DateField()
