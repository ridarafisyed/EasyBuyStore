from django import forms
from .models import Product, Category, Comments


class CategoryForm(forms.ModelForm):
    title =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = Category
        fields = ("title",)

class CommentsForm(forms.ModelForm):
    comments =forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    rate = forms.IntegerField(max_value=5, min_value=1,
        widget=forms.NumberInput( attrs={'step': 1, 'class': 'form-control', 'placeholder': '1', 'default':1 })
    )

    class Meta:
        model = Comments
        fields = ("comments","rate",)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control' 
            }
        )
    )
    
   
    price = forms.DecimalField(max_digits=6, min_value=0,
        widget=forms.NumberInput( attrs={'step': 0.01, 'class': 'form-control' })
    )
    quantity = forms.IntegerField(min_value=0,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control' 
            }
        )
    )
        
    class Meta:
        model = Product
        fields = ("name", "title", 'description', "discount", "disc_value", "category", "price", "quantity","image")
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
            }


