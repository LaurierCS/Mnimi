# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# Create Deck Form
class DeckForm(forms.Form):
    deckName = forms.CharField(label="New Deck Name", max_length=50)

# Create Card Form
class CardForm(forms.Form):
    frontText = forms.CharField(label="Front Text", max_length=280)
    frontImg = forms.FileField(label="Front Image", required=False)
    backText = forms.CharField(label="Back Text", max_length=280)
    backImg = forms.FileField(label="Back Image", required=False)
    
# Edit Card Form
class EditCardForm(forms.Form):
    frontText = forms.CharField(label="Edit Front Text", max_length=280)
    frontImg = forms.FileField(label="Edit Front Image", required=False)
    backText = forms.CharField(label="Edit Back Text", max_length=280)
    backImg = forms.FileField(label="Edit Back Image", required=False)

# Create Account Form
class CreateAccountForm(forms.Form):
    email = forms.CharField(label="Email")
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

# Share Deck Form
class ShareForm(forms.Form):
    username = forms.CharField(label="Username")