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

# checkout/views.py
from .models import Order

def order_success(request):
    latest_order = Order.objects.filter(user=request.user).order_by('-created').first()
    return render(request, 'checkout/success.html', {'order': latest_order})


# orders/views.py ou payments/views.py
from django.shortcuts import render, redirect
from cart.models import Cart
from orders.models import Order  # ou orders.models
from django.contrib.auth.decorators import login_required

@login_required
def checkout_view(request):
    cart = Cart.objects.filter(user=request.user).first()

    if request.method == 'POST':
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        # Crée une commande
        order = Order.objects.create(
            user=request.user,
            cart=cart,
            address=address,
            city="",  # à adapter
            postal_code="",
            paid=True  # à adapter selon paiement
        )

        # Optionnel : vider le panier
        cart.items.all().delete()

        return redirect('orders:order_success')  # ou autre page

    return render(request, 'orders/checkout.html', {'cart': cart})
    

