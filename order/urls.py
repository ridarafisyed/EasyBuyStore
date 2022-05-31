from django.urls import path
from . import views

app_name ="order"
urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('payment/', views.payment, name='payment'),

    path('admin-order-view/',views.admin_order_view, name="admin_order_view"),
    path('admin-order-update/<int:order_id>/',views.admin_order_update, name="admin_order_update"),
    path('admin-order-delete/<int:order_id>/',views.admin_order_delete, name="admin_order_delete"),
    
    path('admin-transaction-history/',views.admin_transaction_history, name="admin_transaction_history"),
    path('admin-transaction-update/<int:order_id>/',views.admin_transaction_update, name="admin_transaction_update"),
    path('admin-transaction-delete/<int:order_id>/',views.admin_transaction_delete, name="admin_transaction_delete"),
    
    path('order-view/',views.order_view, name="order_view"),
    path('order-update/<int:order_id>/',views.order_update, name="order_update"),
    path('order-delete/<int:order_id>/',views.order_delete, name="order_delete"),
    
    path('transaction-history/',views.transaction_history, name="transaction_history"),
    path('transaction-update/<int:order_id>/',views.transaction_update, name="transaction_update"),
    path('transaction-delete/<int:order_id>/',views.transaction_delete, name="transaction_delete"),


]