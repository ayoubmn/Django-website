from django.db import models
from datetime import datetime
# Create your models here.


class Secteur(models.Model):
    namefr = models.CharField(max_length=50)
    namear = models.CharField(max_length=50)

    def __str__(self):
        return self.namefr


class Type(models.Model):
    namefr = models.CharField(max_length=50)
    namear = models.CharField(max_length=20)
    def __str__(self):
        return self.namefr


class pre_post(models.Model):
    namefr = models.CharField(max_length=50)
    namear = models.CharField(max_length=20)

    def __str__(self):
        return self.namefr


class Acctualite(models.Model):
    titre = models.CharField(max_length=400)
    media = models.ImageField(null=True, blank=True)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE, default=0)
    text = models.TextField()
    langue = models.CharField(max_length=10, default=0)

    def __str__(self):
        return str(self.titre)
    class Meta:
        verbose_name = 'Actualite'

class Video(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100,help_text="url de la video  doit etre adapter a l'integration")
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)
    pre_post = models.ForeignKey('pre_post', on_delete=models.CASCADE,default=0)
    langue = models.CharField(max_length=10, default=0)

    def __str__(self):
        return str(self.name)

class Photo(models.Model):
    name = models.CharField(max_length=100)
    url = models.ImageField(null=True, blank=True)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)
    pre_post = models.ForeignKey('pre_post', on_delete=models.CASCADE,default=0)

    def __str__(self):
        return str(self.name)
class Doc(models.Model):
    name = models.CharField(max_length=400)
    url = models.FileField()
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)
    pre_post = models.ForeignKey('pre_post', on_delete=models.CASCADE,default=0)
    langue = models.CharField(max_length=10, default=0)

    def __str__(self):
        return str(self.name)

class Audio(models.Model):
    name = models.CharField(max_length=20)
    url = models.FileField()
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)
    pre_post = models.ForeignKey('pre_post', on_delete=models.CASCADE,default=0)
    langue = models.CharField(max_length=10, default=0)


    def __str__(self):
        return str(self.name)

class Assistance(models.Model):
    titre = models.CharField(max_length=100)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    pre_post = models.ForeignKey('pre_post', on_delete=models.CASCADE,default=0)
    text = models.TextField()
    langue = models.CharField(max_length=10, default=0)

    def __str__(self):
        return str(self.titre)

class Programme(models.Model):
    titre = models.CharField(max_length=400)
    date = models.DateField(max_length=20, default=0)
    text = models.TextField()
    langue = models.CharField(max_length=10, default=0)

    def __str__(self):
        return str(self.titre)

class ContactReception(models.Model):
    nom = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    sujet = models.CharField(max_length=50)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    msg = models.TextField()
    def __str__(self):
        return str(self.nom)

class adresses(models.Model):
    delegation = models.CharField(max_length=100)
    telephone = models.CharField(max_length=100)
    adresse = models.CharField(max_length=1000)
    langue = models.CharField(max_length=10, default=0)

    def __str__(self):
        return str(self.delegation)

class faq(models.Model):
    question = models.CharField(max_length=300)
    reponse = models.TextField()
    langue = models.CharField(max_length=10, default=0)

    def __str__(self):
        return str(self.question)