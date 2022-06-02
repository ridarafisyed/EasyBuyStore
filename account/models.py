from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

CHOICES=[(0,'Client'),
         (1,'Customer')]


class UserAccountManager(BaseUserManager):
    
    def create_user(self,username, first_name, last_name, email,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email)
        user = self.model(username=username, first_name= first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.user_type=1
        user.save()

        return user
    
    def create_superuser(self,username, first_name, last_name, email, password):
        user = self.create_user(username, first_name, last_name, email, password)

        user.is_superuser = True
        user.is_active = True
        user.is_staff = True
        
        user.save()

        return user
    
    def create_client(self, username, first_name, last_name, email, password):
        user = self.create_user(username, first_name, last_name, email, password) 
        
        user.client = True
        user.user_type = 0
        user.save()

        return user

# Create your models here.
class UserAccount(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField('Is Admin', default=False)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_client = models.BooleanField(default = False)
    user_type = models.PositiveIntegerField(choices=CHOICES, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserAccountManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

   
class Store(models.Model):
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(UserAccount, related_name="store",  on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.OneToOneField(UserAccount, related_name="shippment", on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    phone = models.CharField( max_length=50)
    postcode = models.CharField( max_length=50)
    address_line = models.CharField( max_length=255)
    address_line2 = models.CharField( max_length=255, null=True, blank=True)
    town_city = models.CharField( max_length=150)
    delivery_instructions = models.CharField( max_length=255, null=True, blank=True)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True)
    default = models.BooleanField( default=False)

    def __str__(self):
        return self.full_name

