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
        shareForm = ShareForm(request.POST)

        if form.is_valid():
            Deck.createDeck(form.cleaned_data['deckName'], request.user)
            return HttpResponseRedirect("/")
        
        if shareForm.is_valid():
            print("Share form was submitted!")
    else:
        form = DeckForm()
        shareForm = ShareForm()

    # Retrieving users decks
    userDecks = Deck.getUsersDecks(request.user.id)
    decksDueCardsTuple = []
    for deck in userDecks:
        dueCards = CardLedger.getNumberofDueCards(deck.id, request.user.id)
        decksDueCardsTuple.append([deck, dueCards])

    context = {
        "decks": decksDueCardsTuple,
        "form": form,
        "shareForm": shareForm
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
        shareForm = ShareForm(request.POST)

        if form.is_valid():
            Card.createCard(deck, form.cleaned_data, request.user)
            return HttpResponseRedirect(f"/deck/{deckId}")

        if shareForm.is_valid():
            print("Share form was submitted!")
    else:
        form = CardForm()
        shareForm = ShareForm()
    
    deckCards = Card.getDecksCards(deckId)
    if deckCards == False:
        deckCards = "Deck does not exist!"

    context = {
        "deck": deck,
        "deckCards": deckCards,
        "form": form,
        "shareForm": shareForm
    }
    template_name = "app/deck.html"

    return render(request, template_name, context)

@login_required
def study(request, deckId):
    template_name = "app/study.html"
    dueCard = CardLedger.getDueCard(deckId, request.user.id)
    #print(dueCard)
    if dueCard == False:
        context = {
            "studyCardVerify": False
        }
        return render(request, template_name, context)
    
    studyCard = Card.getStudyCard(dueCard[0])
    context = {
        "studyCard": studyCard,
        "ledgerID": studyCard[1],
        "deckID": deckId,
        "studyCardVerify": True
    }
    return render(request, template_name, context)

@login_required
def updateLedger(request, deckId, cardLedgerId, seconds):
    print(deckId)
    print(cardLedgerId)
    print(seconds)

    return HttpResponseRedirect(f"/study/{deckId}")

def create_account(request):
    sentence = "Create Account Page"
    #form_class = UserCreationForm
    template_name = "app/create_account.html"

    if request.method == 'POST':
        form = CreateAccountForm(request.POST)

        if form.is_valid():
            cleanForm = form.cleaned_data
            user = User.objects.create_user(username=cleanForm['username'], email=cleanForm['email'], password=cleanForm['password'])
            user.save()
            user = authenticate(username=cleanForm['username'], password=cleanForm['password'])
            login(request, user)
            return redirect('index')
    
    else:
        form = CreateAccountForm()

    context = {
        "sentence": sentence,
        "form": form,
    }

    template_name = "app/create_account.html"

    return render(request, template_name, context)
