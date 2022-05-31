from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from account.models import Address, UserAccount
from store.models import Product
from order.models import Order, OrderItem
from cart.cart import Cart
from .forms import AddressForm
import uuid

def checkout (request):
    cart = Cart(request)
   
    msg = "You are here in Checkout page "
    if request.method == 'POST':
        if request.user.is_authenticated:
            addressForm = AddressForm(request.POST)
            
            # adding Address
            if addressForm.is_valid():
                cd = addressForm.cleaned_data
                address = Address.objects.create(user = request.user, 
                full_name=cd['full_name'], 
                phone=cd['phone'],
                postcode=cd['postcode'],
                address_line=cd['address_line'],
                address_line2=cd['address_line2'],
                town_city=cd['town_city'],
                delivery_instructions=['delivery_instructions'])
                address.save()
                messages.success(request, "Your Address is successful store!")
            else:
                messages.warning(request, "There must be some error please try again later.. ")
        else:
            msg =msg + "AnonymousUser try to checkout"
            messages.success(request, "Your Address is successful store!")
        
    else:
        addressForm = AddressForm()
        

    

    return render(request, 'store/checkout.html', {'msg': msg, 'addressForm': addressForm})