from store.models import Brand, Category
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}