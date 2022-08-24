from decimal import Decimal
import re
from django.shortcuts import  redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.http import require_POST
from order.models import Order, OrderTransaction
from .models import Store, PaymentDetail, Address, UpgradeTransaction
from store.models import Product
from .forms import LoginForm, PaymentForm, SignUpForm, StoreForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from order.models import BillingAddress,OrderItem
from order.forms import BillingAddressForm

User = get_user_model()


# Create your views here.

# if user want to sell or become a register user for discount 

def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, "Your Account has been Registered Successful!")       
            return redirect('login_view')
        else: 
            messages.warning(request, "The form is not valid. Please Try Again.. ")
    else:
        form = SignUpForm()
    return render(request, 'auth/register.html',{'form': form, 'msg': msg})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username= username, password= password)
            if user is not None:
                login(request, user)
                
                return redirect('dashboard')
            else:
                messages.warning(request, "Invalide Credentials")
                 
        else:
            messages.warning(request,"Validation Error please Try Agian...")
           
            form = LoginForm()    
    return render(request, 'auth/login.html', {'form': form, 'msg': msg})

@login_required
def dashboard_view(request):    
    user = request.user
    
    if user.is_superuser:
        total_stores = Store.objects.all().count()
        total_customers = User.objects.filter(user_type = 1).count()
        total_clients = User.objects.filter(user_type = 0).count()
        total_users = User.objects.all().count()
        total_products = Product.objects.all().count()
        total_orders = Order.objects.all().count()
        total_transactions = UpgradeTransaction.objects.all().count()
        all_transactions = OrderTransaction.objects.all()
        transactions = OrderTransaction.objects.filter(customer = request.user)
        total = 0
        for transaction in transactions:
            total += transaction.amount

        user.balance = total
        all_balance = 0
        for transaction in all_transactions:
            all_balance += transaction.amount

        if total_transactions is None:
            total_transactions = 0

        if total_stores is None:
            total_stores = 0

        if total_customers is None:
            total_customers = 0
        
        if total_clients is None:
            total_clients = 0
        
        if total_users is None:
            total_users = 0
        
        if total_products is None:
            total_products = 0
        
        if total_orders is None:
            total_orders = 0
        

        context = {
            'user' : user,
            'total_customers': total_customers,
            'total_clients': total_clients,
            'total_users': total_users,
            'total_stores': total_stores,
            'total_products':total_products, 
            'total_orders': total_orders,
            'total_transactions': total_transactions,
            'all_balance': all_balance,
            'balance' : user.balance
        }
        return render(request, 'dashboard/admin_main.html', context )

    else:             
        if Store.objects.filter(owner = user).exists():
            store = Store.objects.get(owner = user)
            store_id = store.id
            products =  Product.objects.filter(vendor=request.user)
            total_products = Product.objects.filter(vendor=request.user).count()
            total_orders = OrderItem.objects.filter(store=store_id).count()
            total = 0
            transactions = OrderTransaction.objects.filter(customer = request.user)
            for transaction in transactions:
                total += transaction.amount

            user.balance = total
            
            if total_products is None:
                total_products = 0
            
            if total_orders is None:
                total_orders = 0
        
            return render(request, 'dashboard/main.html', {'user' : user,
            'store':store,
                'total_products':total_products, 
                'total_orders': total_orders,
                'balance' : user.balance})
            
        else: 
            store = None
            products = None
            context = {'user':user, 'store':store, 'products':products}
        return render(request, 'dashboard/main.html', context)

def profile_view(request):
    cc_detail = PaymentDetail.objects.filter(user = request.user)
    billing_address = BillingAddress.objects.filter(customer = request.user)
    address = Address.objects.filter(user = request.user)
    context = { 'cc_detail':cc_detail, 'billing_address':billing_address, 'address': address}
    return render(request, "dashboard/profile.html", context)
def upgrade_account(request):

    return render(request, "dashboard/upgrade_account/upgrade_account.html")

def billing_address(request):
    address = BillingAddress.objects.filter(customer = request.user).exists()
    if address:
        address = BillingAddress.objects.get(customer = request.user)
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
                return redirect('upgrade_account')  
        
    else:
        billingAddressForm = BillingAddressForm()
    return render(request, 'dashboard/upgrade_account/billing_address.html', {'address': address, 'billingAddressForm': billingAddressForm})

def card_detail(request):
    cc_detail = PaymentDetail.objects.filter(user = request.user)
    user = request.user
    form = PaymentForm()
    if request.method == 'POST':
        form  = PaymentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cc_detail is not None:
                cc_detail = PaymentDetail.objects.update(  
                    user = user,
                    cc_fullname = cd['cc_fullname'],
                    cc_number = cd['cc_number'],
                    cc_expiry = cd['cc_expiry'],
                    cc_code = cd['cc_code'],
                    )
            else:
                cc_detail= PaymentDetail.objects.create(  
                    user = user,
                    cc_fullname = cd['cc_fullname'],
                    cc_number = cd['cc_number'],
                    cc_expiry = cd['cc_expiry'],
                    cc_code = cd['cc_code'],
                )
            

            messages.info(request , "Account Upgrade Successfully")
            return redirect('upgrade_confirmation')
    else:
        form = PaymentForm()
    context ={'form': form, 'cc_detail': cc_detail}
    return render(request, 'dashboard/upgrade_account/upgrade_account.html', context)

def upgrade_confirmation(request):

    amount = Decimal(500.00).quantize(Decimal('.01'))
    upgrade_transaction = UpgradeTransaction.objects.create(customer = request.user, amount = amount)
    upgrade_transaction.save()
    request.user.user_type = 0
    request.user.is_client = True
    request.user.save()
    transaction = UpgradeTransaction.objects.filter(customer = request.user).last()
    form = StoreForm()
    if request.method == 'POST':
        form  = StoreForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            store= Store.objects.create(  
                    owner = request.user,
                    name = cd['title']
                )
            store.is_store_active = True
            redirect('dashboard')
    else: 
        form = StoreForm()
            

    context = {'transaction': transaction, 'form':form}
    return render(request, "dashboard/upgrade_account/upgrade_confirmation.html", context)


def create_store(request):
    msg= None
    form = StoreForm()
    if request.method == 'POST':
        form  = StoreForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            store = Store.objects.create(  
                    owner = request.user,
                    name = cd['title']
                )
            
            store.is_store_active = True
            request.user.user_type = 1
            store.save()
            messages.success(request , "Store is created successfully")
            redirect('dashboard')
    else: 
        form = StoreForm()

    context = {'form':form}
    return render(request, "dashboard/upgrade_account/create_store.html", context)

    