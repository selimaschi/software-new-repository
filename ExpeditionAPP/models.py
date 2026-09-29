from django.db import models
from EntreprisesAPP.models import Entreprise
class Expedition(models.Model):
    reference = models.CharField( max_length=8)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_Kg = models.DecimalField(max_digits=10, decimal_places=2)
    date_souhaitee = models.DateField()
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=[('en_cours', 'En cours'), ('terminee', 'Terminée')], default='en_cours')
    entreprise = models.ForeignKey(Entreprise,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

