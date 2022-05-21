from django.http import HttpResponseRedirect
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
            return HttpResponseRedirect("/")
    else:
        form = DeckForm()

    # Retrieving users decks
    userDecks = Deck.getUsersDecks(request.user.id)
    decksDueCardsTuple = []
    for deck in userDecks:
        dueCards = CardLedger.getNumberofDueCards(deck.id, request.user.id)
        decksDueCardsTuple.append([deck, dueCards])

    context = {
        "decks": decksDueCardsTuple,
        "form": form
    }
    template_name = "app/homepage.html"

    return render(request, template_name, context)

@login_required
def deck(request, deckId):
    deck = Deck.getDeck(deckId, request.user.id)
    if deck == False:
        deck = "Deck does not exist!"
    if request.method == 'POST':
        form = CardForm(request.POST, request.FILES)
        if form.is_valid():
            Card.createCard(deck, form.cleaned_data, request.user)
            return HttpResponseRedirect(f"/deck/{deckId}")
    else:
        form = CardForm()
    
    deckCards = Card.getDecksCards(deckId)
    if deckCards == False:
        deckCards = "Deck does not exist!"
    
    context = {
        "deck": deck,
        "deckCards": deckCards,
        "form": form,
    }
    template_name = "app/deck.html"

    return render(request, template_name, context)

@login_required
def study(request, deckId):
    dueCards = CardLedger.getDueCards(deckId, request.user.id)
    print(dueCards)
    context = {
        "dueCards": dueCards
    }
    template_name = "app/study.html"

    return render(request, template_name, context)

def create_account(request):
    sentence = "Create Account Page"
    form_class = UserCreationForm
    template_name = "app/create_account.html"

    if request.method == 'POST':
        form = CreateAccountForm(request.POST)

        if form.is_valid():
            cleanForm = form.cleaned_data
            user = User.objects.create_user(username=cleanForm['username'], email=cleanForm['email'], password=cleanForm['password'])
            user.save()
            return render(request, template_name="app/homepage.html")
    
    else:
        form = CreateAccountForm()

    context = {
        "sentence": sentence,
        "form": form,
    }

    template_name = "app/create_account.html"

    return render(request, template_name, context)
