from django import forms
from django.contrib.auth.forms import UserCreationForm, authenticate, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")  # Include email in the registration form
class customAuthenticationForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        if not User.objects.filter(username=username).exists():
            raise forms.ValidationError("User does not exist.")
        
        user = authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError("Invalid credentials.")
        
        return cleaned_data