from genericpath import exists
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import Address, UserAccount, Store
from store.models import Product
from order.models import Order, OrderItem, Transaction
from cart.cart import Cart
from .forms import AddressForm


@login_required
def checkout (request):
    cart = Cart(request)
    if Order.objects.filter(customer = request.user).exists():
        order = Order.objects.filter(customer = request.user).last()

    # if customer exists
    try:
        total_paid = cart.get_total()
        order, create = Order.objects.get_or_create(customer= request.user,status=1, total_paid=total_paid)
        for item in cart:
            product = Product.objects.filter(id = item['product_id'])
            store = Store.objects.filter(ower = product.vender)
            transaction = Transaction.objects.create(store = store, customer= request.user, amount= order.total_paid)
            OrderItem.objects.get_or_create(order=order, product= product, price=item['price'], quantity=item['quantity'])
    except:
        pass
    address = Address.objects.filter(user = request.user).exists()
    if address:
        address = Address.objects.get(user = request.user)
    if request.method == 'POST':
            addressForm = AddressForm(request.POST)
            # adding Address
        
            if addressForm.is_valid():
                cd = addressForm.cleaned_data
                if address:
                    address= Address.objects.update(  
                    user= request.user, 
                    full_name = cd['full_name'],
                    phone= cd['phone'],
                    postcode= cd['postcode'],
                    address_line= cd['address_line'],
                    address_line2= cd['address_line2'],
                    town_city= cd['town_city'],
                    delivery_instructions= cd['delivery_instructions'],
                    default= cd['default']
                )
                else:
                    instance = addressForm.save(commit=False)
                    instance.user = request.user 
                    instance.save()
                
                messages.success(request , "Address save successfully")
                return redirect('order:payment')  
        
    else:
        addressForm = AddressForm()
    return render(request, 'store/checkout/checkout.html', {'address': address, 'addressForm': addressForm, 'order':order})



def payment(request):
    cart = Cart(request)
    address = Address.objects.get(user = request.user)
    order = Order.objects.filter(customer = request.user).last()
    total_paid = cart.get_total()
    order, create = Order.objects.get_or_create(customer= request.user,status=1, total_paid=total_paid)
        
    cart.clear()
    return render(request, 'store/checkout/payment.html', {'address': address, 'order':order})
