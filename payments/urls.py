from django.urls import path
from . import views


app_name = "payments"

urlpatterns = [
    path('payment_detail/', views.payment_detail, name='payment_detail'),
    path('payment_registration/', views.payment_registration_view, name='payment_registration'),
    # path('checkout/', views.checkout, name='checkout'),
    path('<int:order_id>/', views.payment_detail, name='payment_detail'),
    
]

