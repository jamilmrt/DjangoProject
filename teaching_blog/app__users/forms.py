from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import user_profile


class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        
        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password',
        }

class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea, required=False)
    location = forms.CharField(required=False)
    birth_date = forms.DateField(required=False)
    profile_pic = forms.ImageField(required=False)
    
    user_types = [
        (user_profile.teacher, 'teacher'),
        (user_profile.student, 'student'),
    ]
    user_type = forms.ChoiceField(choices=user_profile.user_types, required=True)

    class Meta:
        model = user_profile
        fields = ('bio', 'location', 'birth_date', 'profile_pic', 'user_type')
