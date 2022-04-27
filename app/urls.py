from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('deck/', views.deck, name='deck'),
    path('study/', views.study, name='study'),
    path('accounts/', include('django.contrib.auth.urls'))
]
