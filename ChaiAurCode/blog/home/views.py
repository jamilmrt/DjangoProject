from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def sad_list(request):
    
    return render(request, 'sad_list.html')