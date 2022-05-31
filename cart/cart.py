from django.conf import settings
from decimal import Decimal
from store.models import Product

class Cart(object):
    # it initialize the cart
    def __init__(self, request):
        self.session = request.session
        # getting cart session id from sessions 
        cart = self.session.get(settings.CART_SESSION_ID)
        # checking cart if it exists or not
        if not cart:
            # if cart is not exists in session we set it with empty dictionary  
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        self.shippment = Decimal(250.25).quantize(Decimal('.01'))
        self.tax = Decimal(15.25).quantize(Decimal('.01'))


    # adding item in cart session with item quantity parameters
    #  and override quantity is by default false 
    def add(self, product, quantity):

        # getting product id 
        product_id = str(product.id)
        
        # checking weather item already in the cart or not? 
        if product_id not in self.cart:
            #  if its not in the cart add the item with quantity 0
            self.cart[product_id] = {'quantity':quantity, 'price':str(product.price)}
            # self.cart[product_id][quantity] = quantity
            print (self.cart)
        else:
            self.cart[product_id][quantity] = quantity

        self.save()
        
    
    def increment(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]["quantity"] += 1
        self.save()

    
    def decrement(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            if  self.cart[product_id]["quantity"] > 0:
                self.cart[product_id]["quantity"] -= 1
            if self.cart[product_id]["quantity"] == 0:
                self.remove(product)
            
        self.save()
    
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
       total = sum(Decimal(item['price']).quantize(Decimal('.01')) *  Decimal(item['quantity']).quantize(Decimal('.01')) for item in self.cart.values())
       return Decimal(total).quantize(Decimal('.01'))
    
    def get_tax(self):
        total = self.get_total_price()
        return Decimal(total * self.tax / 100).quantize(Decimal('.01'))
    
    
    def get_total(self):
        total = self.get_total_price()
        tax_value = total * self.tax / 100
        return  Decimal(total + tax_value + self.shippment).quantize(Decimal('.01'))
   
    def total_items(self):
        return len(self.cart)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
    
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in = product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price']= Decimal(item['price']).quantize(Decimal('.01'))
            total =  Decimal(item['price']).quantize(Decimal('.01')) * Decimal(item['quantity']).quantize(Decimal('.01'))
            item['total_price'] = Decimal(total).quantize(Decimal('.01'))
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def save(self):
        self.session.modified = True