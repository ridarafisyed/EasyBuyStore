from django import forms
from account.models import Store
from django.contrib.auth import get_user_model

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
    CHOICES=[(0,'Client'),
         (1,'Customer')]
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    user_type= forms.CharField(label='Account as a ', widget=forms.RadioSelect(choices=CHOICES))
    
    
    class Meta : 
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'user_type')

class StoreForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Store
        fields = ("title",)

class StoreAdminForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Store
        fields = ("title", 'owner')