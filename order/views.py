from decimal import Decimal
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
            price = Decimal(item['price'])
            quantity = int(item['quantity'])
            store = Store.objects.filter(ower = product.vender)
            order, create= OrderItem.objects.get_or_create(order=order, product= product, price=price, quantity=quantity)
            order.save()
            transaction = Transaction.objects.create(store=store, customer=request.user, amount= order.total_paid)
            transaction.save()

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



# ================================================  Admin level views =========================================== #

def admin_order_view(request):
    return render(request, "dashboard/order/admin/admin_order_view.html")

def admin_order_update(request):
    return render(request, "dashboard/order/admin/admin_order_update.html")

def admin_order_delete(request):
    return render(request, "dashboard/order/admin/admin_order_delete.html")


def admin_transaction_history(request):
    return render(request, "dashboard/transactions/admin/admin_transaction_history.html")

def admin_transaction_update(request):
    return render(request, "dashboard/transactions/admin/admin_transaction_update.html")

def admin_transaction_delete(request):
    return render(request, "dashboard/transactions/admin/admin_transaction_delete.html")


# ===========================================  vender/store owner level views ====================================== #

def order_view(request):
    orders = Order.objects.filter(customer = request.user)
    context = { 'orders':orders}
    return render(request, "dashboard/order/order_view.html", context)

def order_update(request, order_id):
    return render(request, "dashboard/order/order_update.html")

def order_delete(request, order_id):
    order = Order.objects.get(pk=order_id)
    if order is not None:
       order.delete()
       messages.info(request,"successfully deteled!")
    else: messages.info(request, "No record found" )
    return render(request, "dashboard/order/order_delete.html")

def transaction_history(request):
    return render(request, "dashboard/transactions/transaction_history.html")

def transaction_update(request):
    return render(request, "dashboard/transactions/transaction_update.html")

def transaction_delete(request):
   return render(request, "dashboard/transactions/transaction_delete.html")