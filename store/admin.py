from atexit import register
from django.contrib import admin
from store.models import Product, Category, SubCategory, Brand
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Brand)
