from django.contrib import admin
from .models import Usuario, Torneo, Equipos
from FDP.views import *
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Torneo)
admin.site.register(Equipos)