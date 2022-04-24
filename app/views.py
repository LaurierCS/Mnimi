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