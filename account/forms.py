from dataclasses import field
from django import forms
from account.models import PaymentDetail, Store
from django.contrib.auth import get_user_model


from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


User = get_user_model()

from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'username','email',  'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['last_name'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['username'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['email'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['password1'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['password1'].widget.attrs['lable'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control form-control-sm'
        self.fields['password2'].widget.attrs['lable'] = 'Confirm Password '

class StoreForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Store
        fields = ("title",)

class StoreAdminForm(forms.ModelForm):
    name =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Store
        fields = ("name", 'owner')
class PaymentForm(forms.ModelForm):
# forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cc_number = forms.IntegerField(max_value=9999999999999999, min_value=1000000000000000, 
        widget=forms.NumberInput( attrs={'class': 'form-control', 'placeholder': '1111 1111 1111 1111' }))
    
    cc_expiry = forms.CharField(widget=forms.DateInput(format='%m/%Y', attrs={'class': 'form-control datepicker', 'placeholder': 'MM/YY'}))
    
    cc_code = forms.IntegerField(max_value=999, min_value=100, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '111',}) )

    class Meta:
        model = PaymentDetail
        fields = ('cc_fullname', "cc_number","cc_expiry", 'cc_code')
        widgets = {
            "cc_fullname": forms.TextInput(attrs={'class': 'form-control'}), 
 
            }
