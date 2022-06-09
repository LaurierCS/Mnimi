from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='index'),
    path('deck/<int:deckId>/', views.deck, name='deck'),
    path('study/<int:deckId>/', views.study, name='study'),
    path('update/<int:deckId>/<int:cardLedgerId>/<int:seconds>/<int:choice>/', views.updateLedger, name='update' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/create_account', views.create_account, name='create_account'),
    path('delete_card/<int:deckId>/<int:cardId>/', views.delete_card, name='deleteCard'),
    path('delete_deck/<int:deckId>/', views.delete_deck, name='deleteDeck'),
    path('share/<int:deckId>/', views.share, name='share')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)