from django.contrib import admin
from .models import *
from django.urls import path

admin.site.register(Qestions)
admin.site.register(Options)
admin.site.register(CustomerFeedback)
admin.site.register(CustomerResponse)


# Register your models here.
