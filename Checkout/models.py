from django.db import models

# Create your models here.
class Checkout(models.Model):
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField()
    phone_number = models.CharField(max_length=13)
    price = models.FloatField()
    qty = models.CharField(max_length=20)
    total = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    code = models.CharField(max_length=20)
