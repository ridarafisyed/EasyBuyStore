
from order.models import Order
import uuid 

def cart_renderer(request):
    try: 
        cart = Order.objects.get(session_id  = request.session['nonuser'], status = 0)
    except:
        request.session['nonuser'] = str(uuid.uuid4())
        cart = Order.objects.create(session_id  = request.session['nonuser'])
    return {'cart':cart}
