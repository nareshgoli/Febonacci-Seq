from django import forms

from .models import Fib

class FibModelForm(forms.ModelForm):
    class Meta:
        model = Fib
        fields = ['number'] 