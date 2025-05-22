from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, OrderItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from django.conf import settings
import stripe
from payments.models import Payment



stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order_detail.html', {'order': order})

@login_required
def update_order_status(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders:order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/update_order_status.html', {'form': form, 'order': order})

@login_required
def order_summary(request):
    """
    Zeigt eine Zusammenfassung der Bestellung für den aktuellen Benutzer.
    """
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order_summary.html', {'orders': orders})

@login_required
def checkout(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        # Hier könnte die Logik für den Abschluss der Bestellung stehen
        order = Order.objects.create(user=request.user)
        # Nach der Bestellung den Warenkorb leeren
        cart.clear()
        return redirect('orders:order_summary')
    return render(request, 'orders/checkout.html', {'cart': cart})

def checkout(request):
    amount_str = request.POST.get("amount")

    if not amount_str:
        return render(request, "payments/checkout.html", {
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "error": "Bitte geben Sie einen gültigen Betrag ein."
    })

    try:
        amount = int(float(amount_str) * 100)
    except ValueError:
        return render(request, "payments/checkout.html", {
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "error": "Ungültiger Betrag."
    })


        # Stripe-Zahlungsabsicht erstellen
        try:
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency="usd",
                payment_method=request.POST.get("payment_method_id"),
                confirmation_method="manual",
                confirm=True,
            )

            # Zahlung speichern
            payment = Payment.objects.create(
                name=request.POST.get("name"),
                email=request.POST.get("email"),
                amount=amount / 100,  # Betrag wieder in USD/EUR umwandeln
                stripe_payment_id=intent.id,
            )

            return render(request, "payments/payment_success.html", {"payment": payment})

        except stripe.error.CardError as e:
            # Stripe-Fehler abfangen
            return render(request, "payments/payment_failed.html", {"error": str(e)})
    else:
        return render(request, "payments/checkout.html", {"stripe_public_key": settings.STRIPE_PUBLIC_KEY})





