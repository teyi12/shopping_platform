from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('order-list/', views.order_list, name='order_list'), 
    path('checkout/', views.checkout, name='checkout'),  # Definieren des checkout-URLs
    path('order-summary/', views.order_summary, name='order_summary'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),
]








# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.order_list, name='order_list'),
# ]
