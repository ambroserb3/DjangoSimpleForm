# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import * # gives us access to `User`models
from django.contrib import messages # grabs django's `messages` module
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm

# Create your views here.

def index(request):

    # If POST, POST:
    if request.method == "POST":
        # Prepare registration data:
        reg_data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "bio": request.POST["bio"],
            "gender": request.POST["gender"],
            "email": request.POST["email"],
            "password": request.POST["password"],
            "confirm_pwd": request.POST["confirm_pwd"],
        }

    # If GET, load login/registration page:
    else:
        return render(request, "posts/index.html")

def user_login(request):
    # If POST, login:
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'posts/index.html', {'form': form})

def register(request):
    # If POST, POST:
    form = UserRegistrationForm(request.POST or None)
    if request.method == "POST":
        new_user = (request.POST or None)
        new_user.save()
    return render(request, 'posts/registration.html', {'new user', new_user})

