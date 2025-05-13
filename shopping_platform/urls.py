
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.home_view, name='home'),
    path("contact/", views.contact_view, name='contact'),
    path("accounts/", include("accounts.urls")),
    path("cart/", include("cart.urls")),
    path("orders/", include("orders.urls")),
    path("payments/", include("payments.urls")),
    path("shop/", include("shop.urls")),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Standard-Login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Standard-Logout
    path('profile/', auth_views.LogoutView.as_view(), name='profile'), 
    path('about/', views.about_view, name='about'), 
    path('danke/', views.danken_view, name='danke'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
