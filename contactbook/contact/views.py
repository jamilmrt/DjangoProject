from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import registerForm, ContactForm
from .models import Contact

# Create your views here.




def register_view(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = registerForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    allContacts = Contact.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'home.html', context={'allContacts': allContacts})

def create(request):
    contactForm = ContactForm()
    if request.method == 'POST':
        contactForm = ContactForm(request.POST, request.FILES)
        if contactForm.is_valid():
            contact = contactForm.save(commit=False)
            contact.user = request.user
            contact.save()
            return redirect('home')
    else:
        print(contactForm.errors)
    return render(request, 'create.html', {'contactForm': contactForm})

def contactDetail(request, pk):
    contact = Contact.objects.get(pk=pk)
    
    return render(request, 'contactDetail.html', {'contact': contact})