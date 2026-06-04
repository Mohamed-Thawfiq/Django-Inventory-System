from django import forms
from django.forms import ModelForm
from .models import *


class product_forms(ModelForm):
    since = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = customer
        fields = '__all__'

class order_form(ModelForm):

    class Meta:
        model= orders
        fields= ['customer_ref','product_ref','order_num','order_date','quantity']