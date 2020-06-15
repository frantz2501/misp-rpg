from django.db import models

# Create your models here.
class Personne(models.Model):
    CHOIX_DEFAUT = [
        ('T', 'Tyrannique'),
        ('F', 'Faible'),
        ('M', 'Médiocre'),
        ('D', 'Dominé (par sa femme, son conseiller)')
    ]
    nom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=1)
    defaut = models.CharField(max_length=1, choices=CHOIX_DEFAUT)

class Maison(models.Model):
    CHOIX_STATUTS = [
        ('V', 'Vieille famille'),
        ('N', 'Nouvelle famille')
    ]
    CHOIX_AMBIANCE = [
        ('I', 'Intrigues, jalousies, rivalités'),
        ('L', 'Lourd secret/passé'),
        ('D', 'Désespoir, fin de règne'),
        ('T', 'Tristesse, drame récent'),
        ('A', 'Autoritaire, chef de famille très fort'),
        ('F', 'Faible, chef de famille sans autorité, anarchie'),
        ('P', 'Parasite : un conseiller extérieur jouit d\'une influence trop importante')
    ]
    nom = models.CharField(max_length=50)
    statut = models.TextField(max_length=1, choices=CHOIX_STATUTS)
    ambiance = models.TextField(max_length=1, choices=CHOIX_AMBIANCE)
    secret = models.TextField(blank=True)
    CHOIX_RICHESSES = [
        ('F', 'Faibles'),
        ('M', 'Moyennes'),
        ('E', 'Elevées')
    ]
    richesses = models.CharField(max_length=1, choices=CHOIX_RICHESSES)
    chef = models.ForeignKey(Personne, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

