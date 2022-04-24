from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'), path('', views.about, name='about'), path('', views.Deck_Page, name='deck_page'),
]
