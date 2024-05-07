from django.shortcuts import render, redirect
from .models import Contact
from .forms import LoginForm, RegistrationForm, CreateUpdateContactForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "crm/index.html")

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context = {"form":form}
    return render(request, "crm/register.html", context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user=user)
                return redirect("dashboard")
    context = {"form":form}
    return render(request, "crm/register.html", context)

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("logout")

@login_required(login_url="login")
def dashboard(request):
    contacts = Contact.objects.all()
    context = {"contacts":contacts}
    return render(request, "crm/dashboard.html", context)

