# Imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify

# User class
class User(models.Model):
    userId = models.IntegerField(primary_key=True, unique=True)
    userName = models.CharField(unique=True, max_length=20, blank=False)
    password = models.CharField(blank=False, max_length=20)
    email = models.CharField(unique=True, blank=False, max_length=31)

    # User Methods below

# Decks class
class Deck(models.Model):
    objectId = models.IntegerField(primary_key=True, unique=True)
    deckId = models.IntegerField() # Unique Unix Time
    userId = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    creatorID = models.IntegerField()
    deckName = models.CharField(blank=False, max_length=50)
    dateCreated = models.DateField()
    isFavourite = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)
    cardCount = models.IntegerField(default=0)

    # Decks Methods below

# Cards class
class Card(models.Model):
    cardId = models.IntegerField(primary_key=True, unique=True)
    deckId = models.IntegerField()
    creatorID = models.IntegerField()
    front_text = models.CharField(max_length=280)
    frontImg = models.URLField(null=True)
    back_text = models.CharField(max_length=280)
    backImg = models.URLField(null=True)

    # Cards Methods below

# Card ledger class
class cardLedger(models.Model):
    objectId = models.IntegerField(primary_key=True, unique=True)
    userId = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    deckId = models.IntegerField()
    cardId = models.ForeignKey(Card, on_delete=models.DO_NOTHING)
    study_date = models.DateField()
    ELO = models.IntegerField(default= 0 )
    leech = models.IntegerField(default=0)

    # Ledger Methods below