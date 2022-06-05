from unicodedata import category
from django.db import models
from django.template.defaultfilters import slugify
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid
import datetime

User = get_user_model()


def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)
# Create your models here.
# products categories
class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    # slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.title
    @property
    def get_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/no_image.jpg"

class SubCategory(models.Model):
    category = models.ForeignKey(Category,related_name='sub_category', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        unique_together = ('category', 'title',)
        
    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(SubCategory, self).save(*args, **kwargs)

class Brand(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='logos/', null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.title
    @property
    def get_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/no_image.jpg"

# products model with user/store who add and category as foreignkey
class Product(models.Model):
    name = models.CharField(max_length=255)
    vendor = models.ForeignKey(User, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True, null=True)
    discount = models.BooleanField(default=False)
    disc_value = models.DecimalField(max_digits=4, decimal_places=2,default=0, blank=True, null=True)
    disc_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name='products', on_delete=models.CASCADE)
    brands = models.ForeignKey(Brand, related_name='brand_products', on_delete=models.CASCADE)
    model = models.CharField(max_length=255, null=True, blank=True)
    year = models.IntegerField( validators=[MinValueValidator(1984), max_value_current_year])
    color = models.CharField(max_length=255, blank=True )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True, verbose_name="")


    class Meta:
        ordering = ['added_at']
    
    def __str__(self):
        return self.title
    @property
    def get_absolute_url(self):
        return reverse("store:product", kwargs={
            'slug': self.slug
        })
    @property
    def get_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/img/no_image.jpg"

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


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    subject = models.CharField(max_length=255, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    rate = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return self.user + '' + self.product
        

# class WishList(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)