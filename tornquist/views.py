from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

# Create your views here.
def index(request):
    return render(request,'tornquist/publica/index.html')

def gastronomia(request):
    restaurantes = [
        {
            'nombre':'Molino Azul - Sierra de la Ventana',
            'ubicacion': 'Sierra de la Ventana (Bs As - Argentina)',
            'telefono':'(+54) 0291-4941075',
            'direccion':'Av San Martin 114, Sierra de la Ventana Bs. As.',
            'pagina_web':'MolinoAzul.com.ar',
            'url_img':'/static/tornquist/publica/img/molino-azul.jpg',
        },

        {
            'nombre':'Sol y Luna - Sierra de la Ventana',
            'ubicacion': 'Sierra de la Ventana (Bs As - Argentina)',
            'telefono':'(+54) 0291-4941075',
            'direccion':'Av. San Marti 353, Sierra de la Ventana Bs. As.',
            'pagina_web':'MolinoAzul.com.ar',
            'url_img':'/static/tornquist/publica/img/sol-y-luna-restaurante.jpg',
        },

        {
            'nombre':'Restaurant Urbano - Tornquist',
            'ubicacion': 'Tornquist (Bs As - Argentina)',
            'telefono':'(+54) 0291-4941075',
            'direccion':'Drago 53, Tornquist Bs. As.',
            'pagina_web':'RestaurantUrbano.com.ar',
            'url_img':'/static/tornquist/publica/img/restaurantUrbano.jpg',
        },

        {
            'nombre':'Hosteria La Peninsula - Villa Ventana',
            'ubicacion': 'Villa Ventana (Bs As - Argentina)',
            'telefono':'(+54) 0291-4941075',
            'direccion':'Drago 53, Villa Ventana Bs. As.',
            'pagina_web':'LaPeninsula.com.ar',
            'url_img':'/static/tornquist/publica/img/hosteria-la-peninsula.jpg',
        },

        {
            'nombre':'Ristorante Da Roberto - Villa Ventana',
            'ubicacion': 'Villa Ventana (Bs As - Argentina)',
            'telefono':'(+54) 0291-4941075',
            'direccion':'Drago 53, Villa Ventana Bs. As.',
            'pagina_web':'DaRoberto.com.ar',
            'url_img':'/static/tornquist/publica/img/ristoranteDaRoberto.jpg',
        }
    ]
    return render(request,'tornquist/publica/gastronomia.html',{'restaurantes':restaurantes})

def zonasAlojamientos(request):
    return render(request,'tornquist/publica/zonasAlojamientos.html')

def actividades(request):
    return render(request,'tornquist/publica/actividades.html')

def puntosInteres(request):
    return render(request,'tornquist/publica/puntosInteres.html')

def emergencias(request):
    return render(request,'tornquist/publica/emergencias.html')

def contacto(request):
    return render(request,'tornquist/publica/contacto.html')