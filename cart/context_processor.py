from ebstore.store.models import Category
from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}

def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}