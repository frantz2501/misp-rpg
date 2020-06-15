"""misp_rpg URL Configuration

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
    2. Add a URL to urlpatterns:  path('objets/', include('objets.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.liste_articles),
    path('event/<id_event>', views.view_event, name='view_event'),
    path('listevent', views.MISP_list_event),
    path('listreports/<repors_tag>', views.view_by_tags),
    path('articles', views.liste_articles, name='liste_articles'),
    path('affiche_article/<article_id>', views.affiche_article, name='affiche_article'),
    path('article_nouveau', views.article_nouveau, name='article_nouveau'),
    path('categorie_nouveau', views.categorie_nouveau, name='categorie_nouveau'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
