from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    # return HttpResponse("Welcome to Chai Aur Django! This is the home page.")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("This is the about page of Chai Aur Django.")
    return render(request, 'website/about.html')

def contact(request):
    return HttpResponse("This is the contact page of Chai Aur Django.")

