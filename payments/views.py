from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm, PaymentRegistrationForm
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.contrib import messages
from .forms import PaymentRegistrationForm, PaymentForm

import stripe




@login_required
def payment_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.order = order
            payment.save()
            return redirect('orders:order_list')
    else:
        form = PaymentForm()
    return render(request, 'payments/payment_detail.html', {'form': form, 'order': order})


# Stripe-Schlüssel
stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_registration_view(request):
    if request.method == 'POST':
        form = PaymentRegistrationForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)  # Speichert das Formular, aber noch nicht in der Datenbank

            # Versuchen, die Zahlung über Stripe zu erstellen
            try:
                intent = stripe.PaymentIntent.create(
                    amount=int(payment.amount * 100),  # Betrag in Cent
                    currency='usd',
                    payment_method_types=['card'],
                    description=f"Payment by {payment.name}",
                )

                # Speichern der Stripe Payment ID
                payment.stripe_payment_id = intent['id']
                payment.save()

                # Weiterleitung zur Zahlungsseite
                return render(request, 'payments/stripe_payment.html', {
                    'client_secret': intent['client_secret'],
                    'payment': payment,
                })

            except stripe.error.StripeError as e:
                messages.error(request, f"An error occurred: {e.user_message}")
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PaymentRegistrationForm()

    return render(request, 'payments/registration.html', {'form': form})

from django.shortcuts import render
from cart.models import CartItem

def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total = sum(item.total_price() for item in cart_items)

    return render(request, "payments/checkout.html", {
        "cart_items": cart_items,
        "total_amount": total,
    })



