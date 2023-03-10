from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4

# Create your models here.
class ProductInventoryVO(models.Model):
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"


class ClothingInventoryVO(models.Model):
    name = models.CharField(max_length=255)
    product = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class ClothingBox(models.Model):
    name = models.CharField(max_length=100)
    clothing_items = models.ManyToManyField(ClothingInventoryVO)

    def __str__(self):
        return self.name


class ProductsBox(models.Model):
    name = models.CharField(max_length=100)
    product_items = models.ManyToManyField(ProductInventoryVO)

    def __str__(self):
        return self.name


class User(AbstractUser):
    email = models.EmailField(max_length=250, unique=True)
    subscribed = models.BooleanField(default=False)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.email}"


class Subscription(models.Model):
    model_number = models.PositiveSmallIntegerField(unique=True, null=True)
    price = models.PositiveSmallIntegerField(default=30, null=True, blank=True)
    products = models.ForeignKey(
        ProductsBox, on_delete=models.PROTECT, null=True, blank=True
    )
    clothing = models.ForeignKey(
        ClothingBox, on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return f"{self.model_number}"


class Receipt(models.Model):
    firstName = models.CharField(max_length=32)
    lastName = models.CharField(max_length=32)
    email = models.EmailField()
    address = models.CharField(max_length=254)
    address2 = models.CharField(max_length=254)
    country = models.CharField(max_length=254)
    state = models.CharField(max_length=254)
    username = models.CharField(max_length=254)
    orderNumber = models.PositiveIntegerField(unique=True)
    zip = models.CharField(max_length=254)
    price = models.CharField(max_length=50, default="$36.99", null=True, blank=True)

    def __str__(self):
        return f"{self.order_number}"
