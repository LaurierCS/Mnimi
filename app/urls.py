from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('deck/<int:deckId>/', views.deck, name='deck'),
    path('study/<int:deckId>/', views.study, name='study'),
    path('update/<int:deckId>/<int:cardLedgerId>/<int:seconds>/', views.updateLedger, name='update' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create_account', views.create_account, name='create_account'),
]