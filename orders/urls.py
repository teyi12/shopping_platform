from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order-list/', views.order_list, name='order_list'), 
    path('checkout_view/', views.checkout_view, name='checkout_view'),  # Definieren des checkout-URLs
    path('order-summary/', views.order_summary, name='order_summary'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),
    path('update_order_status', views.update_order_status, name='update_order_status'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('success/', views.order_success, name='order_success'),
    path('checkout_address_view/', views.checkout_address_view, name='checkout_address_view')
]








