from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('deck/', views.deck, name='deck'),
    path('study/', views.study, name='study'),
]
