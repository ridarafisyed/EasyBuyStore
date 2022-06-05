from decimal import Decimal
from django.core.mail import send_mail
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from account.models import Address, PaymentDetail, UserAccount, Store
from account.forms import PaymentForm
from store.models import Product
from order.models import BillingAddress, Order, OrderItem, OrderTransaction, PaymentMethod
from cart.cart import Cart
from .forms import AddressForm, PaymentMethodForm, BillingAddressForm

from twilio.rest import Client


# ================================================  Checkout Process views =========================================== #
@login_required
def checkout (request):
    cart = Cart(request)
    address = Address.objects.filter(user = request.user).exists()
    if address:
        address = Address.objects.get(user = request.user)
    if request.method == 'POST':
            addressForm = AddressForm(request.POST)
            # adding Address
            if addressForm.is_valid():
                cd = addressForm.cleaned_data
                address, create = Address.objects.update_or_create(
                    user= request.user, 
                    full_name = cd['full_name'],
                    phone= cd['phone'],
                    street_address= cd['street_address'],
                    state= cd['state'],
                    city= cd['city'],
                    country= cd['country'],
                    postcode= cd['postcode'],
                    delivery_instructions= cd['delivery_instructions']
                )
                address.save()
                messages.success(request , "Address saved successfully")
                return redirect('order:payment_method')  
            else:
                messages.success(request , "Form is invalide please try again..")
    else:
        addressForm = AddressForm()
    return render(request, 'store/checkout/checkout.html', {'address': address, 'addressForm': addressForm})

@login_required
def payment_method(request):
    form = PaymentMethodForm()
    cart = Cart(request)
    
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('order:payment')
    else:
        form = PaymentMethodForm()
    return render(request, 'store/checkout/payment_method.html',{'form': form})

@login_required
def payment(request):
    cart = Cart(request)
    address = BillingAddress.objects.filter(customer = request.user).exists()
    if address:
        address = BillingAddress.objects.filter(customer = request.user).last()
    if request.method == 'POST':
            billingAddressForm = BillingAddressForm(request.POST)
            # adding Address
        
            if billingAddressForm.is_valid():
                cd = billingAddressForm.cleaned_data
                if address:
                    address= BillingAddress.objects.update(  
                    customer= request.user, 
                    first_name = cd['first_name'],
                    last_name = cd['last_name'],
                    street_address = cd['street_address'],
                    city = cd['city'],
                    postcode = cd['postcode'],
                    state = cd['state'],
                    country = cd['country'],
                )
                else:
                    address= BillingAddress.objects.create(  
                    customer= request.user, 
                    first_name = cd['first_name'],
                    last_name = cd['last_name'],
                    street_address = cd['street_address'],
                    city = cd['city'],
                    postcode = cd['postcode'],
                    state = cd['state'],
                    country = cd['country'],
                    )
                
                messages.success(request , "Address save successfully")
                return redirect('order:payment_detail')  
        
    else:
        billingAddressForm = BillingAddressForm()
    return render(request, 'store/checkout/paymentbillingdetail.html', {'address': address, 'billingAddressForm': billingAddressForm})

@login_required

def payment_detail(request):
    cart = Cart(request)
    total_paid = cart.get_total()
    if Order.objects.filter(customer = request.user).exists():
        order = Order.objects.filter(customer = request.user).last()
        # if customer exists
        for item in cart:
            product = Product.objects.get(pk = item['product'].id)
            price = Decimal(item['price'])
            quantity = int(item['quantity'])
            storeowner = product.vendor
            store = Store.objects.get(owner = storeowner)
            user = UserAccount.objects.get(username= storeowner.username)
            user.balance = total_paid
            orderItem= OrderItem.objects.create(order=order, product= product, price=price, quantity=quantity)
            orderItem.save()
            orderTransaction = OrderTransaction.objects.create(store=store, customer=request.user, order= order, amount = price)
            orderTransaction.save()
            messages.success(request , "Address save successfully")
    else:
        # if custumer not exist create one 
        order, create = Order.objects.get_or_create(customer= request.user, status=1, total_paid=total_paid)
        for item in cart:
            product = Product.objects.get(pk = item['product'].id)
            price = Decimal(item['price'])
            quantity = int(item['quantity'])
            storeowner = product.vendor
            store = Store.objects.get(owner = storeowner)
            user = UserAccount.objects.get(username= storeowner.username)
            user.balance = total_paid
            orderItem= OrderItem.objects.create(order=order, product= product, price=price, quantity=quantity,store= store)
            orderItem.save()
            orderTransaction = OrderTransaction.objects.create(store=store, customer=request.user, order= order, amount = price)
            orderTransaction.save()
            messages.success(request , "Address save successfully")
    cart.clear()
    cc_detail = PaymentDetail.objects.filter(user = request.user)
    form = PaymentForm()
    if request.method == 'POST':
        form  = PaymentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cc_detail is not None:
                cc_detail = PaymentDetail.objects.update(  
                    user = request.user,
                    cc_fullname = cd['cc_fullname'],
                    cc_number = cd['cc_number'],
                    cc_expiry = cd['cc_expiry'],
                    cc_code = cd['cc_code'],
                    )
            else:
                cc_detail= PaymentDetail.objects.create(  
                    user = request.user,
                    cc_fullname = cd['cc_fullname'],
                    cc_number = cd['cc_number'],
                    cc_expiry = cd['cc_expiry'],
                    cc_code = cd['cc_code'],
                )
            messages.info(request , "Order Place Successfully")
            return redirect('order:order_confirmation')
    else:
        form = PaymentForm()
    
    return render(request, 'store/checkout/cc_detail.html', {'form':form, 'cc_detail': cc_detail})

def order_confirmation(request):
    cart = Cart(request)
    order = Order.objects.filter(customer = request.user).last()
    order_transaction = OrderTransaction.objects.filter(customer = request.user).last()
    billing_address = BillingAddress.objects.filter(customer = request.user).exists()
    address = Address.objects.get(user = request.user)
    subject = "Order Confirmation"
    message = f"Hi {request.user.first_name} {request.user.first_name}, Your oder {order.order_id} with amount is placed successfully. It will be delivered in 4 - 5 working days. have a nice day."
    send_mail(
     subject,
     message,
    'samplereciver1234@gmail.com',
    ['ridarafisyed@gmail.com'],
    fail_silently=False,
)
    context = {'order': order, 'address': address, 'billing_address': billing_address, 'order_transaction': order_transaction}
    
    return render(request, 'store/checkout/order_confirmation.html', context)

# ================================================  Admin level views =========================================== #
@user_passes_test(lambda u: u.is_superuser)
def admin_order_view(request):
    orders = Order.objects.all()
    orderItems = OrderItem.objects.all()
    context = { 'orders':orders, 'orderItems':orderItems}
    return render(request, "dashboard/order/admin/admin_order_view.html", context)

@user_passes_test(lambda u: u.is_superuser)
def admin_order_update(request, order_id):
    return render(request, "dashboard/order/admin/admin_order_update.html")

@user_passes_test(lambda u: u.is_superuser)
def admin_order_delete(request, order_id):
    order = Order.objects.get(pk=order_id)
    if order is not None:
       order.delete()
       messages.info(request,"successfully deteled!")
    else: messages.info(request, "No record found" )
    return render(request, "dashboard/order/admin/admin_order_delete.html")

@user_passes_test(lambda u: u.is_superuser)
def admin_transaction_history(request):
    transactions = OrderTransaction.objects.filter(customer = request.user)
    context = { 'transactions':transactions}
    return render(request, "dashboard/transactions/admin/admin_transaction_history.html", context )

@user_passes_test(lambda u: u.is_superuser)
def admin_total_transaction_history(request):
    transactions = OrderTransaction.objects.all()
    context = { 'transactions':transactions}
    return render(request, "dashboard/transactions/admin/admin_transaction_history.html", context )

@user_passes_test(lambda u: u.is_superuser)
def admin_transaction_update(request, transaction_id):
    # transaction = Order.objects.get(pk=transaction_id)
    # if transaction is not None:
    #    transaction.delete()
    #    messages.info(request,"successfully deteled!")
    # else: messages.info(request, "No record found" )
    return render(request, "dashboard/transactions/admin/admin_transaction_update.html")

@user_passes_test(lambda u: u.is_superuser)
def admin_transaction_delete(request, transaction_id):
    transaction = Order.objects.get(pk=transaction_id)
    if transaction is not None:
       transaction.delete()
       messages.info(request,"successfully deteled!")
    else: messages.info(request, "No record found" )
    return render(request, "dashboard/transactions/admin/admin_transaction_delete.html")


# ===========================================  vender/store owner level views ====================================== #
@login_required
def order_view(request):
    orders = Order.objects.filter(customer = request.user)
    context = { 'orders':orders}
    return render(request, "dashboard/order/order_view.html", context)

@login_required
def order_update(request, order_id):
    # transaction = Order.objects.get(pk=transaction_id)
    # if transaction is not None:
    #    transaction.delete()
    #    messages.info(request,"successfully deteled!")
    # else: messages.info(request, "No record found" )
    return render(request, "dashboard/order/order_update.html")

@login_required
def order_delete(request, order_id):
    order = Order.objects.get(pk=order_id)
    if order is not None:
       order.status = 2
       messages.info(request,"successfully canceled!")
    else: messages.info(request, "No record found" )
    return render(request, "dashboard/order/order_delete.html")

@login_required
def transaction_history(request):
    transactions = OrderTransaction.objects.filter(customer = request.user)
    context = { 'transactions':transactions}
    return render(request, "dashboard/transactions/transaction_history.html", context)

@login_required
def transaction_update(request, transaction_id):
    return render(request, "dashboard/transactions/transaction_update.html")

@login_required
def transaction_delete(request, transaction_id):
    order = OrderTransaction.objects.get(pk=transaction_id)
    if order is not None:
       order.delete()
       messages.info(request,"successfully deteled!")
    else: messages.info(request, "No record found" )
    return render(request, "dashboard/transactions/transaction_delete.html")