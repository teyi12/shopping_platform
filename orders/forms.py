from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-control'}),
        }



PAYMENT_METHOD_CHOICES = [
    ('credit_card', 'Kreditkarte'),
    ('paypal', 'PayPal'),
    ('bank_transfer', 'Banküberweisung'),
]

class CheckoutForm(forms.Form):
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Adresse'}))
    postal_code = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Postleitzahl'}))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Stadt'}))
    payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect)
