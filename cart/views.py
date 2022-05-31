from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
import uuid
from order.models import Order
from cart.cart import Cart
from cart.forms import CartAddItemForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity']
        )
    return redirect('cart:cart_detail')

def cart_increment(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.increment(product)
    return redirect('cart:cart_detail')

def cart_decrement(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)       
    return render(request, 'store/cart/cart.html', {'cart': cart})