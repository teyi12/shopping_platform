# from django.shortcuts import render, get_object_or_404, redirect
# from django.shortcuts import render, redirect, get_object_or_404
# from orders.models import Order, OrderItem
# from .models import Cart, CartItem
# from .forms import CartItemForm
# from shop.models import Product
# from django.contrib.auth.decorators import login_required


# def cart_detail(request):
#     cart = Cart.objects.get(user=request.user)
#     return render(request, 'cart/cart_detail.html', {'cart': cart})


# @login_required
# def cart_detail(request):
#     cart, _ = Cart.objects.get_or_create(user=request.user)
#     return render(request, 'cart/cart_detail.html', {'cart': cart})

# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart, _ = Cart.objects.get_or_create(user=request.user)
#     if request.method == 'POST':
#         form = CartItemForm(request.POST)
#         if form.is_valid():
#             cart_item = form.save(commit=False)
#             cart_item.cart = cart
#             cart_item.product = product
#             cart_item.save()
#             return redirect('/cart/')
#     else:
#         form = CartItemForm()
#     return render(request, 'cart/add_to_cart.html', {'form': form, 'product': product})






# # Warenkorb aktualisieren
# @login_required
# def add_to_cart_view(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
#     order_item, item_created = OrderItem.objects.get_or_create(order=order, product=product)

#     if not item_created:
#         order_item.quantity += 1
#         order_item.save()

#     return redirect('/cart/')

# @login_required
# def remove_from_cart_view(request, pk):
#     order = Order.objects.filter(user=request.user, is_ordered=False).first()
#     if order:
#         order_item = order.items.filter(id=pk).first()
#         if order_item:
#             order_item.delete()
#     return redirect('/cart/')

# # Warenkorb anzeigen
# # @login_required
# # def cart_view(request):
# #     order = Order.objects.filter(user=request.user, is_ordered=False).first()
# #     if not order:
# #         order_items = []
# #         total = 0
# #     else:
# #         order_items = order.items.all()
# #         total = sum(item.product.price * item.quantity for item in order_items)
# #     return render(request, 'orders/cart.html', {'order_items': order_items, 'total': total})

# # Checkout
# @login_required
# def checkout_view(request):
#     order = Order.objects.filter(user=request.user, is_ordered=False).first()
#     if not order:
#         return redirect('/cart/')

#     if request.method == 'POST':
#         # Beispiel: Stripe-Integration kann hier implementiert werden
#         order.is_ordered = True
#         order.save()
#         return redirect('orders:order_summary')

#     total = sum(item.product.price * item.quantity for item in order.items.all())
#     return render(request, 'orders/checkout.html', {'order': order, 'total': total})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Cart, CartItem
from .models import Product

@login_required
@login_required
def cart_detail(request):
    """Zeigt den Warenkorb des Benutzers an."""
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()  # Hier greifen wir korrekt auf die CartItem-Objekte zu
    total_price = sum(item.total_price() for item in cart_items)  # Gesamtbetrag berechnen
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'cart_items': cart_items, 'total_price': total_price})


@login_required
def add_to_cart(request, product_id):
    """Produkt zum Warenkorb hinzufügen."""
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"{product.name} wurde zum Warenkorb hinzugefügt.")
    return redirect('cart:cart_detail')

@login_required
def update_cart_item(request, item_id):
    """Menge eines Artikels im Warenkorb aktualisieren."""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        if new_quantity > 0:
            cart_item.quantity = new_quantity
            cart_item.save()
            messages.success(request, "Artikelmenge wurde aktualisiert.")
        else:
            cart_item.delete()
            messages.success(request, "Artikel wurde aus dem Warenkorb entfernt.")
        return redirect('cart:cart_detail')
    return render(request, 'cart/update_cart_item.html', {'cart_item': cart_item})

def get_total_price(self):
        """Berechnet den Gesamtpreis."""
        return sum(item['quantity'] * item['price'] for item in self.items)

@login_required
def remove_from_cart(request, item_id):
    """Artikel aus dem Warenkorb entfernen."""
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, "Artikel wurde aus dem Warenkorb entfernt.")
    return redirect('cart:cart_detail')
