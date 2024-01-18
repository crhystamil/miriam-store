from django import forms
from .models import Sale

class SellForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['seller', 'product_inv', 'quantity_sold', 'selling_price', 'registredby']
