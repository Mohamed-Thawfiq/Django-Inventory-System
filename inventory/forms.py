# from django.forms import ModelForm
from .models import *
from django import forms

class product_forms(forms.ModelForm):
    class Meta:
        model=product
        fields='__all__'
        widgets={
            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'product_description':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'tax':forms.NumberInput(attrs={'class':'form-control'}),
            'images':forms.FileInput(attrs={'class':'form-control'}),

        }


