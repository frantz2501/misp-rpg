from django.db import models
from .conf import *

# Create your models here.
class Personne(models.Model):
    nom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1)
    defaut = models.CharField(max_length=1, choices=CHOIX_DEFAUT)

class Maison(models.Model):

    nom = models.CharField(max_length=50)
    statut = models.TextField(max_length=1, choices=CHOIX_STATUTS)
    ambiance = models.TextField(max_length=1, choices=CHOIX_AMBIANCE)
    secret = models.TextField(blank=True)
    richesses = models.CharField(max_length=1, choices=CHOIX_RICHESSES)
    chef = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

