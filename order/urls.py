from django.urls import path
from . import views

app_name ="order"
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),
    path('payment-method/', views.payment_method, name='payment_method'),
    path('payment-detail/', views.payment_detail, name='payment_detail'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
    

    path('admin-order-view/',views.admin_order_view, name="admin_order_view"),
    
    path('admin-order-update/<int:order_id>/',views.admin_order_update, name="admin_order_update"),
    path('admin-order-delete/<int:order_id>/',views.admin_order_delete, name="admin_order_delete"),
    
    path('admin-transaction-history/',views.admin_total_transaction_history, name="admin_total_transaction_history"),
    path('admin-total-transaction-history/',views.admin_transaction_history, name="admin_transaction_history"),
    
    path('order-view/',views.order_view, name="order_view"),

    path('order-update/<int:order_id>/',views.order_update, name="order_update"),
    path('order-delete/<int:order_id>/',views.order_delete, name="order_delete"),
    
    path('transaction-history/',views.transaction_history, name="transaction_history"),
    path('track_order/',views.track_order_view, name="track_order"),



]