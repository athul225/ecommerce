from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.TextField()
    email=models.TextField()
    uname=models.TextField()
    pwd=models.TextField()

class admin(models.Model):
    name=models.TextField()
    email=models.TextField()
    uname=models.TextField()
    pwd=models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    
    def __str__(self):
        return self.name