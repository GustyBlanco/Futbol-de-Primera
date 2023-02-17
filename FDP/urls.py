#from django.contrib import admin
from django.urls import path
from FDP import views
urlpatterns = [
    path('', views.inicio),
    path('Usuario', views.Usuario),
    path('Torneo', views.Torneo),
    path('Equipos', views.Equipos),
]

