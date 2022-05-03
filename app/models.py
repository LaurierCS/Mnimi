# Imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify
from django.core.exceptions import ObjectDoesNotExist

def getUserIDorCreate():
    def_User = User.objects.get_or_create(username = '__defaultUSER__', password = '1234')
    return def_User

# Decks class
class Deck(models.Model):
    deckId = models.IntegerField(primary_key=True) # UUID
    userId =  models.ForeignKey(User, on_delete=models.DO_NOTHING,  default=getUserIDorCreate)
    creatorId = models.IntegerField()
    deckName = models.CharField(blank=False, max_length=50)
    dateCreated = models.DateField()
    isFavourite = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)
    cardCount = models.IntegerField(default=0)

    # Decks Methods below

    def __str__(self):
        return self.deckName

    # returns QuerySet for all decks of User
    def getUsersDecks(user_ID):
        decks = Deck.objects.filter(userId__id = user_ID)
        return decks

    # returns single deck object
    def getDeck(deck_ID, user_ID):
        try:
            deck = Deck.objects.get(deckId = deck_ID, userId__id = user_ID)
        except ObjectDoesNotExist:
            deck = False
        return deck

# Cards class
class Card(models.Model):
    cardId = models.IntegerField(primary_key=True, unique=True)
    deckId = models.ForeignKey(Deck, on_delete = models.DO_NOTHING)
    userId =  models.ForeignKey(User, on_delete=models.DO_NOTHING,  default=getUserIDorCreate)
    study_date = models.DateField(default = None)
    ELO = models.IntegerField(default= 0 )
    leech = models.IntegerField(default=0)
    front_text = models.CharField(max_length=280)
    frontImg = models.URLField(blank=True, null=True)
    back_text = models.CharField(max_length=280)
    backImg = models.URLField(blank=True, null=True)

    # Cards Methods below

    def __str__(self):
        return self.front_text

    # returns all of the cards in a specific users deck
    def getDecksCards(deck_ID, user_ID):
        try:
            cards = Card.objects.filter(deckId = deck_ID, userId__id = user_ID)
        except ObjectDoesNotExist:
            cards = False
        return cards