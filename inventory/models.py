from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255, default='Default Name') 
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
