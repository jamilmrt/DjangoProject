
# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {'title': 'Home', 'message': 'Welcome to the Home Page!'})

def about(request):
    return render(request, 'about.html', {'title': 'About', 'message': 'This is the About Page.'})

def contact(request):
    return render(request, 'contact.html', {'title': 'Contact', 'message': 'Contact us at: example@example.com'})
