from django.db import models
from datetime import datetime

# Create your models here.


class Secteur(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class pre_post(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Acctualite(models.Model):
    titre = models.CharField(max_length=100)
    media = models.CharField(max_length=100)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE, default=0)
    text = models.TextField()



class Video(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)


class Photo(models.Model):
    name = models.CharField(max_length=20, help_text="name.extention ex image.jpg")
    url = models.ImageField(null=True, blank=True)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)
    def __str__(self):
        return str(self.name)
class Doc(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)

class Audio(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    type = models.ForeignKey('Type', on_delete=models.CASCADE,default=0)

class Assistance(models.Model):
    titre = models.CharField(max_length=100)
    date_of = models.DateTimeField(max_length=20, default=datetime.now)
    secteur = models.ForeignKey('Secteur', on_delete=models.CASCADE,default=0)
    pre_post = models.ForeignKey('pre_post', on_delete=models.CASCADE,default=0)
    text = models.TextField()
