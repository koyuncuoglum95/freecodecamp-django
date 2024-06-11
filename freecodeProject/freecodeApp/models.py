from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length= 150)
    img = models.CharField(max_length= 300)


    def __str__(self):
        return f"{self.name}"
    