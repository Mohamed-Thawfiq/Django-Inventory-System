from django.forms import ModelForm
from .models import *

class product_forms(ModelForm):
    class Meta:
        model=product
        fields='__all__'

