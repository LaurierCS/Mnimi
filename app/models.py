# Imports
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify
from django.core.exceptions import ObjectDoesNotExist

def getUserOrCreate():
    def_User = User.objects.get_or_create(username = '__defaultUSER__', password = '1234')
    return def_User

def getDeckorCreate():
    def_User = User.objects.get(username = '__defaultUSER__')
    def_Deck = Deck.objects.get_or_create(user_account = def_User, creator_username = "__defaultUSER__", deckName = "__defaultDeck__")
    return def_Deck

# Decks class
class Deck(models.Model):
    id = models.AutoField(primary_key=True)

    user_account =  models.ForeignKey(User, on_delete=models.DO_NOTHING,  default=getUserOrCreate)
    creator_username = models.CharField(blank=False, max_length=50)
    deckName = models.CharField(blank=False, max_length=50)
    dateCreated = models.DateField(null=True, blank=True)
    isFavourite = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)
    cardCount = models.IntegerField(default=0)

    # Decks Methods below

    def __str__(self):
        return self.deckName

    # returns QuerySet for all decks of User
    def getUsersDecks(user_ID):
        decks = Deck.objects.filter(user_account__id = user_ID)
        return decks

    # returns single deck object
    def getDeck(deck_ID, user_ID):
        try:
            deck = Deck.objects.get(id = deck_ID, user_account__id = user_ID)
        except ObjectDoesNotExist:
            deck = False
        return deck
    def createDeck(deck_name, user_acc):
        new_deck = Deck(user_account = user_acc, creator_username = user_acc.username, deckName = deck_name, dateCreated = datetime.today(), editable = True )
        new_deck.save()
        return


# Cards class
class Card(models.Model):
    id = models.AutoField(primary_key=True)

    deck = models.ForeignKey(Deck, on_delete = models.DO_NOTHING, default=getDeckorCreate)
    
    front_text = models.CharField(max_length=280)
    back_text = models.CharField(max_length=280)
    front_Img = models.ImageField(upload_to='images/', null=True, blank=True)
    back_Img = models.ImageField(upload_to='images/', null=True, blank=True)

    # Cards Methods below

    def __str__(self):
        return self.front_text

    # returns all of the cards in a specific users deck
    def getDecksCards(deck_ID):
        try:
            cards = Card.objects.filter(deck__id = deck_ID)
        except ObjectDoesNotExist:
            cards = False
        return cards

class CardLedger(models.Model):
    id = models.AutoField(primary_key=True)

    deck = models.ForeignKey(Deck, on_delete = models.DO_NOTHING, default=getDeckorCreate)
    user_account = models.ForeignKey(User, on_delete=models.DO_NOTHING,  default=getUserOrCreate)
    card = models.ForeignKey(Card, on_delete=models.DO_NOTHING)

    study_date = models.DateField(default = None)
    ELO = models.IntegerField(default= 0 )
    leech = models.IntegerField(default=0)

    def __str__(self):
        return "User ID: {}, Deck ID: {}, Card ID: {}".format(self.user_account.id, self.deck.id, self.card.id)
    
    def getNumberofDueCards(deck_ID, user_ID):
        dueCards = CardLedger.objects.filter(deck__id = deck_ID, user_account__id = user_ID, study_date__lte = datetime.today()).count()
        return dueCards