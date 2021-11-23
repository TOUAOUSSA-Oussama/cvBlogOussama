from django.shortcuts import render
from . import models
# Create your views here.

## page de garde : mon cv
def principale(request):
    formations = models.Formations.objects.all()
    experiences = models.Experience.objects.all()
    projets = models.Projet.objects.all()
    return render(request, "principale.html", 
        {"formations" : formations, "experiences" : experiences, "projets" : projets})

## page de mes formations:
def formation(request):
    return render(request, "formations.html")