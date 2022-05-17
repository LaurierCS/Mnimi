from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
from .models import *

@login_required
def homepage(request):

    if request.method == 'POST':
        form = DeckForm(request.POST)

        if form.is_valid():
            Deck.createDeck(form.cleaned_data['deckName'], request.user)
    else:
        form = DeckForm()

    # Retrieving users decks
    userDecks = Deck.getUsersDecks(request.user.id)
    decksDueCardsTuple = []
    for deck in userDecks:
        dueCards = CardLedger.getNumberofDueCards(deck.id, request.user.id)
        decksDueCardsTuple.append([deck, dueCards])

    for decks in decksDueCardsTuple:
        print(decks[1])
    context = {
        "decks": decksDueCardsTuple,
        "form": form
    }
    template_name = "app/homepage.html"

    return render(request, template_name, context)

@login_required
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

@login_required
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

def create_account(request):
    sentence = "Create Account Page"

    context = {
        "sentence": sentence,
    }

    template_name = "app/create_account.html"

    return render(request, template_name)
