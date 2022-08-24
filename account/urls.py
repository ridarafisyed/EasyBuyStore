from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_view, name="login_view"),
    path('register/', views.register_view, name="register"),
    path('logout/',auth_views.LogoutView.as_view(), name="logout"),
    path('profile/', views.profile_view, name="profile"),
    path('dashboard/', views.dashboard_view, name="dashboard"),
    path('create-store/', views.create_store, name="create_store"),
    path('upgrade-account/', views.upgrade_account, name="upgrade_account"),
    path('card-detail/', views.card_detail, name="card_detail"),
    path('billing-address/', views.billing_address, name="billing_address"),
    path('upgrade-confirmation/', views.upgrade_confirmation, name="upgrade_confirmation")
]
