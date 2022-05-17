# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class DeckForm(forms.Form):
    deckName = forms.CharField(label="New Deck Name", max_length=50)
    