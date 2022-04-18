# Imports
from django.contrib import admin
from .models import *

# Register your models here.
app_models = [User, Deck, Card, cardLedger]

admin.site.register(app_models)#Model to register in the Admin site)