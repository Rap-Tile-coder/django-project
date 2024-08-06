from django.db import models

# Create your models here.

class Furniture(models.Model):
    furnitureType  = (
        ("bedcott","bedcott"),("sofa-set", "sofa-set"),
        ("chairs","chair"), ("dhiwan","dhiwan"),
        ("pooja stand","pooja stand"),
        ("alamara", "alamara")
    )
    ItemName = models.CharField(max_length=150, choices=furnitureType)
    BrandName = models.CharField(max_length=50)
    RetailPrice = models.CharField(max_length=20)
    SalePrice = models.CharField(max_length=20)
    Quantity = models.IntegerField()