
from django import forms
from .models import CustomerID


class CustIdForm(forms.ModelForm):
    class Meta:
        model=CustomerID
        fields='__all__'
