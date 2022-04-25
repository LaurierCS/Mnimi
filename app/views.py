from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *


def homepage(request):
    sentence = "Home-page"
    context = {
        "sentence": sentence,
    }
    template_name = "app/homepage.html"

    return render(request, template_name, context)

def about(request):
    sentence = "About"
    context = {
        "sentence": sentence,
    }
    template_name = "app/homepage.html"

    return render(request, template_name, context)

def Deck_Page(request):
    sentence = "Deck Page"
    context = {
        "sentence": sentence,
    }
    template_name = "app/homepage.html"

    return render(request, template_name, context)

# auth main view
def auth_view(request):
    page_title = "Login"
    registration_form = RegistrationForm()
    
    context = {
        'page_title': page_title,
        'registration_form': registration_form,
    }
    
    template_name = 'app/auth.html'
    
    return render(request, template_name, context)

# registration main view
def registration_view(request):
    page_title = "Register"
    
    context = {
        'page_title': page_title,
    }
    
    template_name = 'app/registration.html'

# login main view
def login_view(request):
    page_title = "Login"
    
    context = {
        'page_title': page_title,
    }
    
    template_name = 'app/login.html'
    
# login handler
def login_handler(request):
    if request.user.is_authenticated:
        print("already logged in")
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            print("logged in")
            return redirect('home')
        
        else:
            messages.info(request, "username or password is incorrect")
            
    return

# registration handler
def registration_handler(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'account created')
            print("account created")
            
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
    return