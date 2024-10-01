from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    telephone = models.CharField(max_length=11, default="")
    province = models.CharField(max_length=20, default="")
    district = models.CharField(max_length=30, default="")
    address = models.TextField(max_length=200, default="")
    number = models.IntegerField(null=True, blank=True)
    size = models.TextField(max_length=10, default="")
    colour = models.CharField(max_length=30, default="")
    payment_method = models.TextField(max_length=70, default="")
    product_id = models.IntegerField(null=True, blank=True)
    date = models.TextField(max_length=100, default="")

    def __str__(self):
        return f"Ürün adı:{self.product_id} Adet:{self.number} Beden:{self.size} Renk:{self.colour}"