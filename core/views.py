from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products':products})

def about(request):
    return render(request, 'about.html', {})

# The login function
def login_user(request):
    if request.method == "POST":
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You have been logged in "))
            return redirect('index')
        else:
            messages.success(request,("There was an error please try again"))
            return redirect("login")
    else:
        return render(request, 'login.html', {})

# The logout function
def logout_user(request):
    logout(request)
    messages.success(request, ("You have successfully logged out "))
    return redirect("index")

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # login user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered successfully, welcome !!! "))
            return redirect('index')
        else:
            messages.success(request, ("oops tthere was a problem registering you "))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form':form})
    
def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, "product.html", {'product':product})