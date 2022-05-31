from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.http import require_POST
from order.models import Order


from .models import Store
from store.models import Product, Category
from .forms import LoginForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.

# if user want to sell or become a register user for discount 

def register_view(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.user_type == 0:
                store = Store.objects.create(name=user.username, created_by=user)
                store.save()
                messages.info(request, "Your Vendor Account has been Registered Successful!")
               
            else: 
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
        }
        return render(request, 'dashboard/admin_main.html', context )

    else:             
        if user.user_type == 0 :
            store = request.user.store
            products =  Product.objects.filter(vendor=request.user)
        else: 
            store = None
            products = None
        return render(request, 'dashboard/main.html', {'user':user, 'store':store, 'products':products})
