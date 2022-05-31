
from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddItemForm(forms.Form):
    quantity = forms.IntegerField(max_value=10, min_value=0,
        widget=forms.NumberInput( attrs={'step': 1, 'class': 'form-control' })
    )


