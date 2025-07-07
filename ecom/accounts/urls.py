from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path("accounts/", views.login_page, name="login"),
    path('admin/', admin.site.urls),
]