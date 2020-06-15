"""campagne_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.liste, name='liste'),
    path('nouvellemaison/', views.saisie_maison, name='crea_maison'),
    path('nouvellepersonne/', views.saisie_personne, name='crea_personne'),
    path('affichemaisons/', views.affiche_maisons, name='affiche_maisons'),
    path('affichepersonnes/', views.affiche_personnes, name='affiche_personnes'),
]
