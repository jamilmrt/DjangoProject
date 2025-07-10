# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import registerView



class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    # phone_no = forms.CharField(max_length = 20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    # password = forms.CharField(max_length=65, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email',  'first_name', 'last_name', 'password1', 'password2']