
from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
import uuid
User = get_user_model()


# Create your models here.
# products categories
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

# products model with user/store who add and category as foreignkey
class Product(models.Model):
    name = models.CharField(max_length=255)
    vendor = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    discount = models.BooleanField(default=False)
    disc_value = models.PositiveIntegerField(default=0, blank=True, null=True)
    disc_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name="")
    # thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    class Meta:
        ordering = ['-added_at']
    
    def __str__(self):
        return self.title
    @property
    def get_absolute_url(self):
        return reverse("store:product", kwargs={
            'slug': self.slug
        })
    @property
    def get_add_to_cart_url(self):
        return reverse("store:add-to-cart", kwargs={
            'slug': self.slug
        })

    # to get the products by category
    @property
    def get_products(self):
     return Product.objects.filter(category__title=self.title)


    @property
    def get_total_price(self):
        # if the discount was place on product it will calcualte and give a new price after applying discount 
        if self.discount: 
            
            if self.disc_value > 0:
                # if discount value is given it calcuate accordingly 
                price =   self.disc_price = self.price - (self.disc_value/100 * self.price  )
            else: 
                # if the discount value no mentioned it but user want to give discount it will calculate with 25% 
                price = self.disc_price = self.price - (25/100 * self.price)
        else:
            
            price = self.price 
        return price
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        
        super(Product, self).save(*args, **kwargs)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    # cart_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    device = models.CharField(max_length=100)

    @property
    def num_of_items(self):
        cart_item = self.cartitems_set.all()
        total = sum([qty.quantity for qty in cart_item])
        return total
    
    @property
    def cart_total(self):
        cart_item = self.cartitems_set.all()

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


# class SaveItem(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     session_id = models.CharField(max_length=100)
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
