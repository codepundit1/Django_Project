from django.contrib import admin
from .models import *

##Custom sitting for admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'description']
    search_fields = ['category_name']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    search_fields = ['email', 'phone']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'product_category', 'product_quantity']
    search_fields = ['product_name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','customer_id', 'product_id', 'quantity', 'delivary']
    search_fields = ['order_id']
admin.site.register(Category, CategoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
# Register your models here.
