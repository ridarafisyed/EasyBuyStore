from django.urls import path
from . import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    # general Views 
    path('', views.store_view, name="index" ), 
    path('product-view/<slug>/',views.product_detail_view,name='product_view'),  
    path('products-list-view/',views.products_list_view,name='products_list_view'),  
    path('products-category-view/<int:pk>/',views.products_category_view,name='products_category_view'), 
    path("search/", views.search, name="search"),

    # admin level URLs
    # products CURD URLs
    path('admin-products-views', views.admin_products_view, name="admin_products_views"),
    path('admin-product-add-view', views.admin_products_view, name="admin_product_add_view"),
    path('admin-product-edit-view/<slug>/', views.admin_product_edit_view, name='admin_product_edit_view'),
    path('admin-product-delete-view/<slug>/', views.admin_product_delete_view, name='admin_product_delete_view'),

    # stores CURD URLs
    path('admin-stores-view', views.admin_stores_view, name="admin_stores_view"),
    path('admin-store-add-view', views.admin_store_add_view, name="admin_store_add_view"),
    path('admin-edit-store/<int:pk>/', views.admin_store_edit_view, name='admin_edit_store'),
    path('admin-delete-store/<int:pk>/', views.admin_store_delete_view, name='admin_delete_store'),

    # users CURD URLs
    path('admin-users-view', views.admin_users_view, name="admin_users_view"),
    path('admin-users-add', views.admin_user_add_view, name="admin_users_add"),
    path('admin-users-edit/<int:pk>/', views.admin_user_edit_view, name="admin_users_edit"),
    path('admin-users-delete/<int:pk>/', views.admin_user_delete_view, name="admin_users_delete"),
    
    # categories URLs

    path('admin-categories-views', views.admin_categories_view, name="admin_categories_views"),
    path('admin-add-category/', views.admin_category_add_view, name="admin_add_category"),
    path('admin-edit-category/<int:pk>/', views.admin_category_edit_view, name='admin_edit_category'),
    path('admin-delete-category/<int:pk>/', views.admin_category_delete_view, name='admin_delete_category'),

    # dashbaord main 
    # vendor views
    path('store-dashboard/', views.vendor_dashoard_view, name="store_dashoard"),
    
    
    # products CURD URLs
    path('products-view/', views.vendor_products_view, name="vendor_products"),
    path('add-product/', views.product_add_view, name="add_product"),
    path('edit-product/<slug>/', views.product_edit_view, name='edit_product'),
    path('delete-product/<slug>/', views.product_delete_view, name='delete_product'),
    
    # category CURD URLs
    path('dashboard/categories/', views.vendor_categories_view, name="categories"),
    path('add-category/', views.category_add_view, name="add_category"),
    path('edit-category/<int:pk>/', views.category_edit_view, name='edit_category'),
    path('delete-category/<int:pk>/', views.category_delete_view, name='delete_category'),
   
]
