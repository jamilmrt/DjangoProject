from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class registerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password', '').lower()
    #     username = cleaned_data.get('username', '').lower()
    #     email = cleaned_data.get('email', '').lower()
        
    #     if username in password or email.split('@')[0] in password:
    #         raise ValidationError("Password is too similar to username or email.")

    #     return cleaned_data

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    