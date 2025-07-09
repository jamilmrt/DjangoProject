from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect




# Create your views here.

@login_required
def home(request):
    return render(request, "home.html")

def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

