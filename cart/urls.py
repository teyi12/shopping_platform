from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_detail/', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('update_cart_item/<int:item_id>/', views.update_cart_item, name='update_cart_item'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    
    path('get_total_price/', views.get_total_price, name='get_total_price'),
]
