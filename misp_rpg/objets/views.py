from django.shortcuts import render
from .models import Personne, Maison
from .forms import MaisonForm, PersonneForm
# Create your views here.


def liste(requests):
    maisons = Maison.objects.all()
    personnes = Personne.objects.all()
    return render(requests, 'objets/liste.html', {'maisons': maisons, 'personnes':personnes})

def saisie_maison(requests):
    form=MaisonForm(requests.POST or None)
    if form.is_valid():
        form.save()
    return render(requests, 'objets/saisie_maison.html', {'form': form})

def saisie_personne(requests):
    form=PersonneForm(requests.POST or None)
    if form.is_valid():
        form.save()
    return render(requests, 'objets/saisie_personne.html', {'form': form})

def affiche_maisons(requests):
    maisons=Maison.objects.all()
    return render(requests, 'objets/affiche_maisons.html', {'maisons': maisons})

def affiche_personnes(requests):
    personnes=Personne.objects.all()
    return render(requests, 'objets/affiche_personnes.html', {'personnes': personnes})