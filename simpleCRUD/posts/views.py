# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.models import * # gives us access to `User`models
from django.contrib import messages # grabs django's `messages` module
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.

def index(request):

    # If POST, register:
    if request.method == "POST":
        # Prepare registration data:
        reg_data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "bio": request.POST["bio"],
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
        login_data = {
            "email": request.POST["login_email"],
            "password": request.POST["login_password"],
        }

def logout(request):
    """Logs out current user."""

    # Try deleting session and send success message:
    try:
        # Deletes session:
        del request.session['user_id']
        # Adds success message:
        messages.add_message(request, LOGOUT_SUCC, "Successfully logged out.", extra_tags="logout_succ")
    except KeyError: # If `user_id` is not found pass
        pass

    # Return to index page:
    return redirect("/")

