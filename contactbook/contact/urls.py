from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('create/', views.create, name='create'),
    path('contactDetail/<int:pk>', views.contactDetail, name='contactDetail'),
]

