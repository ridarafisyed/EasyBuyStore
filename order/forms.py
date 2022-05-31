from django import forms

from account.models import Address



class AddressForm(forms.ModelForm):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    postcode = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    address_line = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    address_line2 = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    town_city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    default = forms.BooleanField()
    delivery_instructions = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    
    class Meta:
        model = Address
        fields = ("full_name", "phone", "postcode", "address_line", "address_line2", "town_city", "delivery_instructions", "default")
        

