from django.db import models

# Create your models here.
class Product(models.Model):
    Name = models.CharField(max_length=100)
    Price = models.IntegerField()
    Code= models.CharField(max_length=100)

    def __str__(self):
        return super(Product, self).__str__()
