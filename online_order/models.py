from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import SET_DEFAULT, SET_NULL
from django.db.models.fields import CharField, DecimalField

# Create your models here.



class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name




class Category(models.Model):
    category_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.ForeignKey(Category, null=True, blank=True, related_name='category', on_delete=SET_NULL)
    product_quantity = models.CharField(max_length=100, null=True, blank=True)


    def __str__(self):
        return self.product_name

class Order(models.Model):
    delivary_status = {
        ("Pending", "Pending"),
        ("Out of delivary", "Out of delivary"),
        ("Delivered", "Delivered"),
    }

    customer_id = models.ForeignKey(Customer, null=True, blank=True, related_name='customer', on_delete=SET_NULL)
    product_id = models.ForeignKey(Product, null=True, blank=True, related_name='product', on_delete=SET_NULL)
    quantity = models.CharField(max_length=100, null=True, blank=True)
    delivary = models.CharField(max_length=100, null=True, blank=True, choices=delivary_status)

    def __str__(self):
        return self.customer_id.name +", "+ self.product_id.product_name