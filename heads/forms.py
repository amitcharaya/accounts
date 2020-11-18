
from django import forms
from .models import CustomerID


class CustIdForm(forms.ModelForm):
    class Meta:
        model=CustomerID
        fields='__all__'
        widgets={
            'name': forms.TimeInput(attrs={'class':'form-control'}),
            'father_name': forms.TimeInput(attrs={'class': 'form-control'})
        }