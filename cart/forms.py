
from email.policy import default
from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddItemForm(forms.Form):
    quantity = forms.IntegerField(max_value=3, min_value=1,  initial=1,
        widget=forms.NumberInput( attrs={'step': 1, 'class': 'form-control', 'placeholder': '1', 'default':1 })
    )

class CartAddSingleItemForm(forms.Form):
    quantity = forms.IntegerField(max_value=3, min_value=1,  initial=1, 
        widget=forms.HiddenInput())

