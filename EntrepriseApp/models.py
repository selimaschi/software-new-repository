from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError

#validators 
def validate_email(value):
    if not value:
        raise ValidationError("L'adresse e-mail ne peut pas être vide.")
    if not value.endswith('@gmail.com'):
        raise ValidationError("L'adresse e-mail doit se terminer par '@gmail.com'.")
    matricule_fiscale_validator = RegexValidator(regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$', message="Le format du matricule fiscale est invalide. Il doit être au format 1234567/A/B/C/123.")

class Utilisateur(AbstractUser):
    user_id = models.CharField(primary_key=True,max_length=8)
    email = models.EmailField(unique=True,validators=[validate_email])
    telephone = models.CharField(max_length=15,blank=True,null=True)
    role = models.CharField(max_length=20,choices=[('admin','Admin'),('c','Chargeur'),('t','Transporteur')],default='c')

    @classmethod
    def _generate_user_id(cls):
        annee = timezone.now().strftime('%Y')
        prefixe = f"{annee}user"
        dernier = (cls.objects.filter(user_id__startswith=prefixe).order_by('user_id').first())
        compteur = (int(dernier.user_id[-2:]) + 1 if dernier else 1 )
        if compteur > 99:
            raise ValidationError("Le compteur a dépassé la limite maximale de 99.")

        return f"{prefixe}{compteur:02d}"

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._generate_user_id()

        self.full_clean() 
        super().save(*args, **kwargs)





class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200,blank=False, null=False)
    matricule_fiscale = models.CharField(max_length=17,unique=True)
    adresse = models.TextField(validators=[MinLengthValidator(20,"l'adresse doit contenir au moins 20 caractères")])
    type_entreprise = models.CharField(max_length=100,choices=[('c','Chargeur'),('t','Transporteur')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    gerant = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='entreprise')
    

