
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.text import slugify
from django.contrib import messages

from .models import  Brand, Category, Comments, Product
from account.models import Store
from account.forms import StoreForm, StoreAdminForm, SignUpForm
from .forms import CommentsForm, ProductForm, CategoryForm, SearchForm

from cart.forms import CartAddItemForm, CartAddSingleItemForm
from django.db.models import Q 
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()
# Create your views here.

# ================================================  general level views =========================================== #

# this is the main page view when you enter the store 
def store_view(request):
    deals = Product.objects.filter(discount= True).order_by('-id')[:8][::-1]
    products = Product.objects.order_by('-id')[:20][::-1]
    single_form = CartAddSingleItemForm()
    context= {'deals':deals, 'products': products, "single_form": single_form}
    return render(request,'index.html', context)

# products detail views 
def product_detail_view(request, slug): 
   product=Product.objects.get(slug=slug) 
   comments = Comments.objects.filter(product = product)
   same_category_products = Product.objects.filter(category = product.category)
   same_brand_products = Product.objects.filter(brands = product.brands)
   form = CartAddItemForm()
   singleForm = CartAddSingleItemForm()
   commentform = CommentsForm()
   context= {'product':product, 'comments' : comments,'form':form, 'single_form': singleForm, 'commentform': commentform,'same_category': same_category_products, 'same_brand': same_brand_products}
   return render(request, "store/products/view_product.html", context )
   

def products_list_view(request):
    deals = Product.objects.filter(discount= True)
    categories = Category.objects.all()
    brand = Brand.objects.all()
    products = Product.objects.all()
    single_form = CartAddSingleItemForm()
    context= {'deals':deals, 'categories': categories, 'products': products, 'brand': brand, "single_form":single_form}
    return render(request, "store/products/view_products.html", context )

def products_category_view(request, pk):
    categories = Category.objects.all()
    deals = Product.objects.filter(discount= True)
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category = category)
    single_form = CartAddSingleItemForm()
    brand = Brand.objects.all()

    context= {'deals':deals,  'products': products, 'category': category,'categories': categories, 'brand': brand, 'single_form': single_form}
    return render(request, "store/products/products_category.html", context )

def categories_list_view(request):
    categories = Category.objects.all()
    context= { 'categories': categories }
    return render(request, "store/products/categories_list_view.html", context )

def hotdeals_list_view(request):
    deals = Product.objects.filter(discount = True)
    single_form = CartAddSingleItemForm()
    context = {'deals': deals, 'single_form':single_form}
    return render(request, "store/products/hotdeal_list_view.html", context)

def brands_list_view(request):
    brands = Brand.objects.all()
    context = {'brands': brands}
    return render(request, "store/products/brands_list_view.html", context)

def products_brands_view(request, pk):
    categories = Category.objects.all()
    deals = Product.objects.filter(discount= True)
    brand = Brand.objects.get(pk=pk)
    products = Product.objects.filter(brands = brand)
    single_form = CartAddSingleItemForm()
    brand = Brand.objects.all()

    context= {'deals':deals,  'products': products, 'categories': categories, 'brand': brand, 'single_form':single_form}
    return render(request, "store/products/products_category.html", context )

def add_review(request, pk):
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid:
            user = request.user
            product = Product.objects.get(pk = pk)
            comment = Comments.objects.create(user=user, product= product,comment=request.POST['comments'], rate=request.POST['rate'])
            comment.save()
            messages.info(request, "Your review is submitted successfully!")
            return HttpResponseRedirect(request.path_info)
    return HttpResponseRedirect(request.path_info)

def search(request):
    categories = Category.objects.all()
    single_form = CartAddSingleItemForm()
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(Q(title__contains = searched)| Q(description__contains= searched))
        categories = Category.objects.all()
        context = {'products': products, "query": searched, 'categories':categories, 'single_form':single_form}
        return render(request, "store/products/search_products.html", context )
    context = { 'categories':categories}
    return render(request, "store/products/search_products.html", context )

    
# ==================================================  Admin Level views ============================================= #
# ====================================================  Products views ============================================== #


# list of all products and its detail 
@user_passes_test(lambda u: u.is_superuser)
def admin_products_view(request):
    products =  Product.objects.all()
    total = products.count()

    context = {'products': products, 'total': total}
    return render(request, 'dashboard/products/admin/admin_products.html', context)

# edit any product detail 
@user_passes_test(lambda u: u.is_superuser)
def admin_product_edit_view(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()

            return redirect('products')
    else:
        form = ProductForm(instance=product)
    
    context =  {'form': form, 'product': product}
    return render(request, 'dashboard/products/edit_product.html', context)

# delete any products regardless of user or store 
@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete_view(request, slug):
    product = Product.object.get(slug=slug)
    if product is not None:
       product.delete()
       messages.info(request, "successfully deteled!")
    else: messages.error(request,"No record found")

    return render(request, 'dashboard/products/admin/delete_product.html')

# ====================================================  Store views ============================================== #

# list of all stores register in website
@user_passes_test(lambda u: u.is_superuser)
def admin_stores_view(request):
    stores =  Store.objects.all()
    total = stores.count()
    return render(request, 'dashboard/stores/admin_stores_view.html', {'stores': stores, 'total': total})
@user_passes_test(lambda u: u.is_superuser)
def admin_store_add_view(request):
    msg = None
    if request.method == "POST":
        form = StoreAdminForm(request.POST)
        if form.is_valid():
            store = form.save()
            messages.info(request, "Store save successfully")
            return redirect('admin_stores_view')
        else:
           messages.info(request, "The form is not valid please try again...")
    else:
        form = StoreAdminForm()
    return render(request, "dashboard/stores/admin_store_add.html", {'form': form, "msg": msg})


# edit any product detail 
@user_passes_test(lambda u: u.is_superuser)
def admin_store_edit_view(request,pk):
    store = Store.objects.get(pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        
        if form.is_valid():
            form.save()

            return redirect('stores')
    else:
        form = StoreForm(instance=store)
    
    return render(request, 'dashboard/stores/admin_store_edit.html', {'form': form, 'store': store})

# delete any products regardless of user or store 
@user_passes_test(lambda u: u.is_superuser)
def admin_store_delete_view(request, pk):
    store = Store.objects.get(pk=pk)
    if store is not None:
       store.delete()
       messages.info(request,"successfully deteled!")
    else: messages.error(request,"No record found")

    return render(request, 'dashboard/stores/admin_store_delete.html')

# =================================================  Customer/ User views ========================================== #
# list all the customers that dont have any store in website
@user_passes_test(lambda u: u.is_superuser)
def admin_users_view(request):
    customers =  User.objects.filter(user_type = 1)
    clients =  User.objects.filter(user_type = 0)
    users =  User.objects.all()
    stores =  Store.objects.all()
    total_stores = stores.count()
    total_customers = customers.count()
    total_clients = clients.count()
    total_users = users.count()

    context = {
        'customers': customers, 'total_customers': total_customers,
        'clients': clients, 'total_clients': total_clients,
        'users': users, 'total_users': total_users,
        'stores': stores, 'total_stores': total_stores,
        }
    return render(request, 'dashboard/accounts/admin_user_view.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_add_view(request):
    customers =  User.objects.filter(user_type = 1)
    clients =  User.objects.filter(user_type = 0)
    users =  User.objects.all()
    total_customers = customers.count()
    total_clients = clients.count()
    total_users = users.count()
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.info(request, "Account has been Registered Successful!")       
            return redirect('admin_users_view')
        else: 
            messages.warning(request, "The form is not valid. Please Try Again.. ")
    else:
        form = SignUpForm()

    context = { 'form': form, 'msg':msg }
    return render(request, 'dashboard/accounts/admin_user_add.html', context)


# edit any User detail 
@user_passes_test(lambda u: u.is_superuser)
def admin_user_edit_view(request,pk):
    store = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()

            return redirect('stores')
    else:
        form = ProductForm(instance=store)
    return render(request, 'dashboard/accounts/admin_user_edit.html', {'form': form, 'store': store})

# delete any products regardless of user or store 
@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete_view(request, pk):
    msg = None
    user = User.objects.get(pk=pk)
    if user is not None:
       user.delete()
       messages.info(request,"successfully deteled!")
       
    else: 
        messages.info(request, "No record found" )

    return render(request, 'dashboard/accounts/admin_user_delete.html', {'msg': msg})
# ====================================================  Category views ============================================== #
# list all the categories mentioned in the website
@user_passes_test(lambda u: u.is_superuser)
def admin_categories_view(request):
    categories =  Category.objects.all()
    total = categories.count()
    return render(request, 'dashboard/categories/admin/admin_categories.html', {'categories': categories, 'total': total})


# user can edit their own products 
@login_required
def vendor_product_edit_view(request, pk):
    vendor = request.user
    product = vendor.products.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()

            return redirect('products')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'dashboard/products/admin/edit_product.html', {'form': form, 'product': product})

# user can delete their own products 


@login_required
def vendor_categories_view(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories/admin/categories.html', {'categories': categories})

@login_required
def admin_category_edit_view(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'dashboard/categories/admin/edit_category.html', {'form': form, 'category': category})
    
@login_required
def admin_category_delete_view(request, pk):
    msg = None
    category = Category.objects.get(pk=pk)
    if category is not None:
       category.delete()
       messages.info(request , "successfully deteled!")
    else:  messages.error(request ,  "No record found")
    return render(request, 'dashboard/categories/admin/delete_category.html',{'msg': msg})

@login_required
def admin_category_add_view(request):
    msg = None
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.info(request , "Category save successfully")
            return redirect('categories')
        else:
            messages.error(request , "the form is not valid please try again...")
    else:
        form = CategoryForm()
    return render(request, "dashboard/categories/admin/add_category.html", {'form': form, "msg": msg})



# ===========================================  vender/store owner level views ====================================== #


# store owner or vender who wants to sell the things can perfom curd operations on their products 

# main dashboard view for venders
@login_required
def vendor_dashoard_view(request):
    name = request.user.first_name
    products = request.user.products
    return render (request, "dashboard/dashboard.html", {'name': name, 'products': products})

# can view their own products and can edit or delete them 
@login_required
def vendor_products_view(request):
    products =  Product.objects.filter(vendor=request.user)
    total = products.count()
    return render(request, 'dashboard/products/products.html', {'products': products, 'total': total})

# add product to their store 
@login_required
def admin_product_add_view(request):
    msg = None
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vendor = request.user 
            instance.slug= slugify(instance.title)
            instance.save()
            messages.info(request , "Product save successfully")
            return redirect('products')
    else:
        form = ProductForm()

    return render(request, "dashboard/products/admin/add_product.html", {'form': form})

# add product to their store 
@login_required
def product_add_view(request):
    msg = None
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.vendor = request.user 
            instance.slug= slugify(instance.title)
            instance.save()
            messages.info(request , "Product save successfully")
            return redirect('products')
    else:
        form = ProductForm()

    return render(request, "dashboard/products/add_product.html", {'form': form})

# user can edit their own products 
@login_required
def product_edit_view(request, pk):
    vendor = request.user
    product = vendor.products.get(pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        
        if form.is_valid():
            form.save()

            return redirect('products')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'dashboard/products/edit_product.html', {'form': form, 'product': product})

# user can delete their own products 
@login_required
def product_delete_view(request, pk):
    msg = None
    vendor = request.user
    product = vendor.products.get(pk=pk)
    if product is not None:
       product.delete()
       messages.info(request , "successfully deteled!")
    else: messages.error(request , "No record found")

    return render(request, 'dashboard/products/delete_product.html')


@login_required
def vendor_categories_view(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/categories/categories.html', {'categories': categories})

@login_required
def category_edit_view(request, pk):
    category = Category.objects.get(pk=pk)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForm(instance=category)
    
    return render(request, 'dashboard/categories/edit_category.html', {'form': form, 'category': category})
    
@login_required
def category_delete_view(request, pk):
    msg = None
    category = Category.objects.get(pk=pk)
    if category is not None:
       category.delete()
       messages.info(request , "successfully deteled!")
    else:  messages.error(request ,  "No record found")
    return render(request, 'dashboard/categories/delete_category.html',{'msg': msg})

@login_required
def category_add_view(request):
    msg = None
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.info(request , "Category save successfully")
            return redirect('categories')
        else:
            messages.error(request , "the form is not valid please try again...")
    else:
        form = CategoryForm()
    return render(request, "dashboard/categories/add_category.html", {'form': form, "msg": msg})


