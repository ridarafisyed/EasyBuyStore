import uuid
import os
from django.db import models
from django.conf import settings
from account.models import Store
from store.models import Product


CHOICES=[(0,'debit/credit'),
         (1,'cash on delivery')]

STATUS =[(0,'approved'),
         (1,'pending'),
         (2,'cancel'),
         (3,'delivered')]


class Order(models.Model):
    order_id = models.UUIDField(default = uuid.uuid4, editable = False)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(choices=STATUS, default=0)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    billing_satuts = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="order_items", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="order_items")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0, null=True, blank=True)

class OrderTransaction(models.Model):
    transaction_id = models.UUIDField(default = uuid.uuid4, editable = False)
    store =  models.ForeignKey(Store, on_delete=models.CASCADE, related_name="transaction",  null=True, blank=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transaction",  null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="transaction")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)

class PaymentMethod(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payment_method", null=True, blank=True)
    method = models.PositiveIntegerField(choices=CHOICES, default=1)

class BillingAddress(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="billing")
    email =models.CharField(max_length=255)
    first_name =  models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    state= models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at= models.DateTimeField(auto_now=True)
