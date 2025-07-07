"""Models for the products app."""

from django.db import models
from django.contrib.auth.models import User
from base.models import BaseModel


# Create your models here.
class Category(BaseModel):
    """Model representing a product category."""
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")

    def __str__(self):
        return f"{self.category_name}"

class Product(BaseModel):
    """Model representing a product."""
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    product_price = models.IntegerField()
    product_description = models.TextField()
    product_image = models.ImageField(upload_to="products")

    def __str__(self):
        return f"{self.product_name} - {self.category.category_name}"

class ProductImage(BaseModel):
    """Model representing additional images for a product."""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product_images")

class Cart(BaseModel):
    """Model representing a user's cart."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name="carts")
    product_price = models.IntegerField()
    product_qty = models.IntegerField(default=1)
    total_price = models.IntegerField()

    def __str__(self):
        return f"{self.product} - {self.user}"


