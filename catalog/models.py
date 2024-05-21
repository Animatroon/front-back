from django.db import models

# Create your models here.
class Catalog(models.Model):

    name = models.TextField()
    file = models.FileField(upload_to='catalogs/')

    
class Reestr(models.Model):

    name = models.TextField()
    # file = models.FileField(upload_to='reestrs/')

class SubReestr(models.Model):
    title = models.TextField()
    fk = models.ForeignKey(to=Reestr, on_delete=models.CASCADE)

class PoiskPravoobladateley(models.Model):

    name = models.TextField()
    performer = models.TextField()  
    individ_face = models.TextField()
    repertoire = models.TextField()
    contract_number = models.TextField()
    datу_of_signing = models.DateField(null=True,  default=None)
    file = models.FileField(upload_to='PoiskPravoobladateley/')



class InostrannyeOkupy(models.Model):

    text = models.TextField()
    title = models.CharField(max_length=255)
    