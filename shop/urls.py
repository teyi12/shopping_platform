from django.urls import path
from . import views

app_name = "shop"
urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('categories/', views.category_list_view, name='category_list'),
]
