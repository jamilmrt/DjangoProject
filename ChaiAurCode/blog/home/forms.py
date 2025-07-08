from django import forms
from .models import RHome


class RHomeForm(forms.ModelForm):
    class Meta:
        model = RHome
        fields = ['text'] 
    