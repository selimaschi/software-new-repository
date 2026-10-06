from django.db import models
from EntreprisesAPP.models import Entreprise
from django.core.validators import MinValueValidator
class vehicule(models.Model):
    immatriculation = models.CharField(primary_key=True, max_length=10)
    type_vehicules = models.CharField(max_length=20,choices=[('m','Mercedes'),('f','Ford'),('b','Bugatti')],default='m')
    capacite_Kg = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(1,"la capacité doit être supérieure à 0")])
    entreprise = models.ForeignKey(Entreprise,on_delete=models.CASCADE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   
   