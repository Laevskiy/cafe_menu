from django import forms
from .models import *

class AddOrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'