from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

def homepage(request):
    sentence = "Home-page"
    # Retrieving users decks
    userDecks = Deck.getUsersDecks(request.user.id)
    print(userDecks)
    context = {
        "sentence": sentence,
        "decks": userDecks
    }
    template_name = "app/homepage.html"

    return render(request, template_name, context)

def deck(request, deckId):
    sentence = "Deck Page"
    userDeck = Deck.getDeck(deckId, request.user.id)
    if userDeck == False:
        userDeck = "Deck does not exist!"
    print(userDeck)
    context = {
        "sentence": sentence,
        "userDeck": userDeck
    }
    template_name = "app/deck.html"

    return render(request, template_name, context)

def study(request, deckId, cardId):
    sentence = "Study Page"
    # userCards = Card.getDecksCards(deckId, request.user.id)
    # if userCards == False:
    #     userCards = "Deck does not exist!"
    # print(userCards)

    context = {
        "sentence": sentence,
       #"userCards": userCards
    }
    template_name = "app/study.html"

    return render(request, template_name, context)
