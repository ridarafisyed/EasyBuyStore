from django.contrib import admin
from order.models import Order, OrderItem,Transaction

# Register your models here.

admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Transaction)
