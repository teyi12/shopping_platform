# from django import forms
# from .models import Payment


# class PaymentForm(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ['stripe_payment_id', 'amount']
#         widgets = {
#             'stripe_payment_id': forms.TextInput(attrs={'class': 'form-control'}),
#             'amount': forms.NumberInput(attrs={'class': 'form-control'}),
#         }


from django import forms
from .models import Payment

class PaymentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['name', 'email', 'amount']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name on Card'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['stripe_payment_id', 'amount']
        widgets = {
            'stripe_payment_id': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        def clean_amount(self):
            amount = self.cleaned_data.get('amount')
            if amount <= 0:
                raise forms.ValidationError("Der Betrag muss größer als 0 sein.")
            return amount
