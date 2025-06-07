from django.db import models
from django.utils import timezone

class Payment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_payment_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    order = models.OneToOneField("orders.Order", on_delete=models.CASCADE, null=True, blank=True)  # relation fixe

    def __str__(self):
        return f"Payment by {self.name} - ${self.amount}"
