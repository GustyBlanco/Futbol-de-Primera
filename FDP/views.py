from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, 'FDP/inicio.html')
    #return HttpResponse("Inicio")

def Usuario(request):
    return render(request, 'FDP/usuario.html')
    #return HttpResponse("Usuario")

def Torneo(request):
    return render(request, 'FDP/torneo.html')
    #return HttpResponse("Torneo")

def Equipos(request):
    return render(request, 'FDP/equipos.html')
    #return HttpResponse("Equipos")