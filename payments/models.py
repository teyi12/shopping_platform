# from django.db import models
# from django.contrib.auth.models import User
# from orders.models import Order

# class Payment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     stripe_payment_id = models.CharField(max_length=100, unique=True)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20, choices=[
#         ('Pending', 'Pending'),
#         ('Completed', 'Completed'),
#         ('Failed', 'Failed'),
#     ], default='Pending')

#     def __str__(self):
#         return f"Payment {self.stripe_payment_id}"



from django.db import models

from django.utils import timezone  # <- Ajoute ça en haut

class Payment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)  # <- Modifié

    def __str__(self):
        return f"Payment by {self.name} - ${self.amount}"

