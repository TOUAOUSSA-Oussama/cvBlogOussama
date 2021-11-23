from django.db import models

# Create your models here.

## modele pour les formations :
class Formations(models.Model):
    anneeDebut = models.CharField(max_length=4)
    anneeFin = models.CharField(max_length=4)
    description = models.CharField(max_length=400)
    lieu = models.CharField(max_length=100)

## modele pour les projets :
class Projet(models.Model):
    nom = models.CharField(max_length=100)
    environnement = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    lienGithub = models.CharField(max_length=100)

## modele pour experience professionnelle :
class Experience(models.Model):
    role = models.CharField(max_length=100)
    nomEntreprise = models.CharField(max_length=100)
    dateDebut = models.CharField(max_length=100)
    dateFin = models.CharField(max_length=100)
    description = models.CharField(max_length=400)