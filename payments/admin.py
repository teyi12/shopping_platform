from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'created_at')
    search_fields = ('name', 'email', 'stripe_payment_id')


