from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'), 
    path('about', views.about, name='about'), 
    path('deckpage', views.Deck_Page, name='deck_page'),
    path('auth', views.auth_view, 'auth'),
    path('register', views.registration_view, name='register'),
    path('login', views.login_view, name='login'),
]