from django.db import models
from django.conf import settings
from account.models import Store
from store.models import Product


CHOICES=[(0,'cart'),
         (1,'ordered'),
         (2,'delivered'),
         (3,'received')]


class Transaction(models.Model):
    store =  models.ForeignKey(Store, on_delete=models.CASCADE, related_name="transaction",  null=True, blank=True)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="transaction",  null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    added_date = models.DateTimeField(auto_now_add=True)


class Order(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="order",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.PositiveIntegerField(choices=CHOICES, default=0)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    billing_satuts = models.BooleanField(default=False)

    class Meta:
        ordering = ('created_at',)
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="order_items")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    # @property
    # def get_total(self):
    #     return self.quantity * self.product.get_final_price()

    # @property
    # def get_final_price(self):
    #     return self.get_total_product_price()
    


    