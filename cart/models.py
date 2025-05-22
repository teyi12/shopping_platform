from django.db import models
from django.contrib.auth.models import User
from shop.models import Product
from django.conf import settings

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"Cart of {self.user.username}"
    
    def total_price(self):
        return sum(item.total_price() for item in self.items.all())
    
    def clear(self):
        """Löscht alle Artikel im Warenkorb."""
        self.items.all().delete()
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"

    def clear(self):
        """Löscht alle Artikel im Warenkorb."""
        self.items.all().delete()
    


