# Imports
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify

# Decks class
class Deck(models.Model):
    deckId = models.IntegerField(primary_key=True) # UUID
    userId =  models.IntegerField(default=0)
    creatorId = models.IntegerField()
    deckName = models.CharField(blank=False, max_length=50)
    dateCreated = models.DateField()
    isFavourite = models.BooleanField(default=False)
    editable = models.BooleanField(default=False)
    cardCount = models.IntegerField(default=0)

    # Decks Methods below

# Cards class
class Card(models.Model):
    cardId = models.IntegerField(primary_key=True, unique=True)
    deckId = models.ForeignKey(Deck, on_delete = models.DO_NOTHING)
    userId = models.IntegerField(default=0)
    study_date = models.DateField(default = None)
    ELO = models.IntegerField(default= 0 )
    leech = models.IntegerField(default=0)
    front_text = models.CharField(max_length=280)
    frontImg = models.URLField(null=True)
    back_text = models.CharField(max_length=280)
    backImg = models.URLField(null=True)

    # Cards Methods below