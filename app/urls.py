from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('deck/<int:deckId>/', views.deck, name='deck'),
    path('study/<int:deckId>/<int:cardId>/', views.study, name='study'),
    path('accounts/', include('django.contrib.auth.urls')),
]