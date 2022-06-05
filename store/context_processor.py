from store.models import Brand, Category


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def brands(request):
    brands = Brand.objects.all()
    return {'brands': brands}