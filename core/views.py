from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {'products':products})

def about(request):
    return render(request, 'about.html', {})

def category(request, foo):
    # replacing hyphen from the request with spaces
    foo = foo.replace('-', ' ')
    try:
        # look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(Category=category)
        return render(request, "category.html", {'products':products, 'category':category})
    except:
        messages.success(request,("That category doesnt exist"))
        return redirect("index")

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

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST or None, instance=current_user)
        
        if form.is_valid():
            form.save()
            login(request, current_user)
            messages.success(request, ("User has been Updated"))
            return redirect("index")
        return render(request, 'update_user.html', {"form":form})
    else:
        messages.success(request, ("You have to login first"))
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

def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})