from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
    return render(request, 'register.html')