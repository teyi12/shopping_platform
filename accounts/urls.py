from django.contrib import admin
from django.urls import path
from . import views




app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),  # Hier wird der logout-Name definiert
    path('profile/', views.profile, name='profile'),
]

