from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from .forms import LoginForm, UserRegisterForm
from django.contrib.auth.forms import UserCreationForm







# Create your views here.
@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')


def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Invalid User Credential')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    # return render(request,template_name='login.html', context={"authenticatonForm":  authenticationForm})
    
def logout(request):
    if request.method == 'POST':
        # logout(request) <-- if i set this line here this occur error 
        auth_logout(request)
        return redirect('/login/')
    return render(request, 'logout.html')


# def registerView(request):
#     userCreationForm = UserCreationForm()
#     if request.method == 'POST':
#         userCreationForm = UserCreationForm(request, data=request.POST or None)
#         if userCreationForm.is_valid():
#             userCreationForm.save()
#             username = userCreationForm.cleaned_data['username']
#             password = userCreationForm.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                     login(request, user)
#                     return redirect('/login/')
#             else:
#                 userCreationForm.add_error(None, 'Invalid User Credential')
#     else:
#         userCreationForm = UserCreationForm()
            
#     return render(request, 'register.html', {'userCreationForm': userCreationForm}) 

def registerView(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally log the user in after registration:
            # login(request, user)
            # if user is not None:
            #     login(request, user)
            return redirect('login/')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})