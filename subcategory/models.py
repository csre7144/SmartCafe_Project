from django.db import models
from Category.models import Category
# Create your models here.

class SubCategory(models.Model):
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    SubCategory_name = models.CharField(max_length=20)
    status = models.BooleanField(default=False)