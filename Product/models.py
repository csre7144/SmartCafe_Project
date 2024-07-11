from django.db import models
from Category.models import Category
# Create your models here.
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(upload_to='img/Productsimg/')
    Desc = models.TextField()
