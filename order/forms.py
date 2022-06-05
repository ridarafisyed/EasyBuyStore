from django import forms

from account.models import Address
from order.models import BillingAddress, PaymentMethod



class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ("full_name", "phone", "street_address",
            "city", "postcode", "state", "country", "delivery_instructions")
        widgets = {
            "full_name": forms.TextInput(attrs={'class': 'form-control'}), 
            "phone": forms.TextInput(attrs={'class': 'form-control'}), 
            "street_address": forms.TextInput(attrs={'class': 'form-control'}),
            "city": forms.TextInput(attrs={'class': 'form-control'}), 
            "postcode": forms.TextInput(attrs={'class': 'form-control'}), 
            "state": forms.TextInput(attrs={'class': 'form-control'}), 
            "country": forms.TextInput(attrs={'class': 'form-control'}), 
            "delivery_instructions": forms.TextInput(attrs={'class': 'form-control'})
            }

class PaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethod
        fields = ("method",)
        widgets = {
            'method' : forms.Select(attrs={'class': 'form-control'}),
         }

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ("email", "first_name", "last_name", "street_address",
            "city", "postcode", "state", "country",)
        widgets = {
            "email": forms.EmailInput(attrs={'class': 'form-control'}), 
            "first_name": forms.TextInput(attrs={'class': 'form-control'}), 
            "last_name": forms.TextInput(attrs={'class': 'form-control'}), 
            "street_address": forms.TextInput(attrs={'class': 'form-control'}),
            "city": forms.TextInput(attrs={'class': 'form-control'}), 
            "postcode": forms.TextInput(attrs={'class': 'form-control'}), 
            "state": forms.TextInput(attrs={'class': 'form-control'}), 
            "country": forms.TextInput(attrs={'class': 'form-control'}),
         }