from django import forms
from .models import Order


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['product', 'quantity', 'border']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'border': forms.Select(attrs={'class': 'form-control'}),
        }
