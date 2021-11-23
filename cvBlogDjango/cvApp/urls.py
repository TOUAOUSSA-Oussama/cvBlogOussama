from django.urls import path
from . import views

## Definition des urls de l'app :
urlpatterns = [
    # page de garde : mon CV
    path('', views.principale, name="mon CV"),
    path('formation', views.formation, name="mes formations")
]