from django.db import models
from EntreprisesAPP.models import Entreprise
from django.core.exceptions import ValidationError
class Expedition(models.Model):
    reference = models.CharField( max_length=8)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_Kg = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(0.001,"le poids doit être supérieur à 0")])
    date_souhaitee = models.DateField()
    description = models.TextField()
    statut = models.CharField(max_length=20, choices=[('en_cours', 'En cours'), ('terminee', 'Terminée')], default='en_cours')
    entreprise = models.ForeignKey(Entreprise,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     
     def clean(self):
        super().clean()
        if selfentreprise _id and self.entreprise.type_entreprise != 'c':
            raise ValidationError("L'entreprise associée à l'expédition doit être de type 'Chargeur'.")

@classmethod
def _generate_reference(cls):
    annee = timezone.now().strftime('%Y')
    prefixe = f"EXP_{annee}_"
    dernier = (cls.objects.filter(reference__startswith=prefixe).order_by('-reference').last())
    compteur = (int(dernier.reference[-5:]) + 1 if dernier else 1 )
    if compteur > 99999:
        raise ValidationError("Le compteur a dépassé la limite maximale de 99999.")

    return f"{prefixe}{compteur:05d}"

def save(self, *args, **kwargs):
    if not self.reference:
        self.reference = self._generate_reference()

    self.full_clean() 
    super().save(*args, **kwargs)



     