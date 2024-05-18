from django.db import models

# Create your models here.
class leakeddb(models.Model):
    email = models.CharField(primary_key=True, max_length=100)
    pwd = models.CharField(max_length=200)
    ipaddr = models.CharField