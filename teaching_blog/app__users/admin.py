from django.contrib import admin
from .models import user_profile
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(user_profile)