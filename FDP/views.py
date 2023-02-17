from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return HttpResponse("Inicio")

def Usuario(request):
    return HttpResponse("Usuario")

def Torneo(request):
    return HttpResponse("Torneo")

def Equipos(request):
    return HttpResponse("Equipos")