from django.shortcuts import render, redirect
from .models import Contact
from .forms import LoginForm, RegistrationForm, CreateUpdateContactForm
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
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
    return render(request, "crm/login.html", context)

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    return redirect("logout")

@login_required(login_url="login")
def dashboard(request):
    contacts = Contact.objects.all()
    context = {"contacts":contacts}
    return render(request, "crm/dashboard.html", context)

@login_required(login_url="login")
def create_record(request):
    form = CreateUpdateContactForm()
    if request.method == "POST":
        form = CreateUpdateContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"form":form}
    return render(request, "crm/create-record.html", context)

@login_required(login_url="login")
def view_record(request, pk):
    contact = Contact.objects.get(id=pk)
    context = {"contact":contact}
    return render(request, "crm/view-record.html", context)

@login_required(login_url="login")
def update_record(request, pk):
    contact = Contact.objects.get(id=pk)
    form = CreateUpdateContactForm(instance=contact)
    if request.method == "POST":
        form = CreateUpdateContactForm(data=request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {"form":form}
    return render(request, "crm/update-record.html", context)

@login_required(login_url="login")
def delete_record(request, pk):
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("dashboard")
    context = {"contact":contact}
    return render(request, "crm/delete-record.html", context)