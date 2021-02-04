from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.FloatField(default=0)

    def __str__(self):
        return self.name
    