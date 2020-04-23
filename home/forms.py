from django import forms
from .models import AddQuote


class QuoteForm(forms.ModelForm):
    class Meta:
        model = AddQuote
        fields = ['o_id', 'customer_name', 'lead_name', 'term_type', 'product', 'penalties']
        widgets = {
            'o_id': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'lead_name': forms.Select(attrs={'class': 'form-control'}),
            'term_type': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'penalties': forms.Select(attrs={'class': 'form-control'}),
        }
