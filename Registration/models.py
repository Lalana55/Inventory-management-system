from django.db import models

# Create your models here.

class Product(models.Model):
    item_code = models.CharField(max_length=200, null=True)
    item_name = models.CharField(max_length=200, null=True)
    unit_price = models.CharField(max_length=200, null=True)
    qty = models.CharField(max_length=200, null=True)
    total_val = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.item_code
