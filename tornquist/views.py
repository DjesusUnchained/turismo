from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.template import loader

from tornquist.models import Gastronomia, Actividades, PuntosInteres, ZonasAlojamientos, Consulta, TipoConsulta

from tornquist.forms import ContactoForm, RegistrarUsuarioForm

from django.contrib import messages


from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
    if(request.method == 'POST'):
        contacto_form = ContactoForm(request.POST)
        if (contacto_form.is_valid()):
            #deberia agregar las acciones que necesito hacer
            
            contacto_form.save()
            messages.success(request,'Hemos recibido tu consulta, en breve te responderemos.')
            messages.info(request,'Te estará llegando un email.')
            contacto_form = ContactoForm()
        else:
            messages.warning(request,'Por favor revisa los errores del formulario.')

    else:
        contacto_form = ContactoForm()
        
    return render(request,'tornquist/publica/contacto2.html',{'contacto_form':contacto_form})

def EditarContacto(request,id_consulta):
    try:
        consulta = Consulta.objects.get(pk=id_consulta)
        contact = Consulta.objects.all()
    except Consulta.DoesNotExist:
        return render(request,'tornquist/publica/index.html')
    if(request.method == 'POST'):
        formulario = ContactoForm(request.POST,instance=consulta)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Hemos editado su consulta')
    else:
       formulario = ContactoForm(instance=consulta)
    return render(request,'tornquist/publica/contacto.html',{'contacto_form':formulario,'consultas': contact})

def login(request):
    if request.method == 'POST':
        # AuthenticationForm_can_also_be_used__
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get('next',None)
            if nxt is None:
                return redirect('inicio')
            else:
                return redirect(nxt)
        else:
            messages.error(request, f'Cuenta o password incorrecto, realice el login correctamente')
    form = AuthenticationForm()
    return render(request, 'tornquist/publica/login.html', {'form': form})

def registrarse(request):
    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            form.save()        
            messages.success(
                request, f'Tu cuenta fue creada con éxito! Ya puedes loguearte')
            return redirect('login')
    else:
        form = RegistrarUsuarioForm()
    return render(request, 'tornquist/publica/registrarse.html', {'form': form})