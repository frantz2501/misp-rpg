from django.shortcuts import render
from .models import Personne, Maison
from .forms import MaisonForm, PersonneForm
# Create your views here.

def saisie_maison(requests):
    form=MaisonForm(requests.POST or None)
    if form.is_valid():
        form.save()
    return render(requests, 'objets/saisie_maison.html', {'form': form})

def saisie_personn(request):
    form=PersonneForm(request.POST or None)
    if form.is_valid():
        form.save()


def affiche_ts_objets(request):
    maisons=Maison.objects.all()
    personnes=Personne.objects.all()