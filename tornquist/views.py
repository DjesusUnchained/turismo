from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

from tornquist.models import Gastronomia, Actividades, PuntosInteres, ZonasAlojamientos

# Create your views here.
def index(request):
    return render(request,'tornquist/publica/index.html')

def gastronomia(request):
    restaurantes = Gastronomia.objects.all
    return render(request,'tornquist/publica/gastronomia.html',{'restaurantes':restaurantes})

def zonasAlojamientos(request):
    alojamientos = ZonasAlojamientos.objects.all
    return render(request,'tornquist/publica/zonasAlojamientos.html',{'alojamientos':alojamientos})

def actividades(request):
    actividades = Actividades.objects.all
    return render(request,'tornquist/publica/actividades.html',{'actividades':actividades})

def puntosInteres(request):
    puntosInteres = PuntosInteres.objects.all
    return render(request,'tornquist/publica/puntosInteres.html',{'puntosInteres':puntosInteres})

def emergencias(request):
    return render(request,'tornquist/publica/emergencias.html')

def contacto(request):
    return render(request,'tornquist/publica/contacto.html')