from django import forms
from .models import Comp

class CompForm(forms.ModelForm):
    class Meta:
        model=Comp
        exclude=['user']
        fields='__all__'