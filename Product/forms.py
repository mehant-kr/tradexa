
from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name of the Product'}))
    weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'in kg'}))
    price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'in INR'}))

    class Meta:
        fields = ('name', 'weight', 'price')
        model = Product

    def save(self, commit=True):
        user = super(ProductCreateForm ,self).save(commit=False)
        if commit:
            user.save()
        return user