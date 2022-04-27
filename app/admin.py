# Imports
from django.contrib import admin
from .models import *

# Register your models here.
app_models = [Deck, Card]

# Model to register in the Admin site)
admin.site.register(app_models)