from django.urls import path
from . import views

app_name ="order"
urlpatterns = [
    path('checkout/', views.checkout, name='checkout')
    # path('add-to-cart/<slug>/', views.add_to_cart, name='add-to-cart'),
    # path('remove-from-cart/<slug>/', views.remove_from_cart, name='remove-from-cart'),
    # path('remove-item-from-cart/<slug>/', views.remove_single_item_from_cart, name='remove-single-item-from-cart'),
]