from django.shortcuts import render
from .models import Zapatilla

def index(request):
    return render(request, 'zapatillasweb/index.html')

def login_view(request):
    return render(request, 'zapatillasweb/login.html')
def registrar_view(request):
    return render(request, 'zapatillasweb/registrar.html')

def home(request):
    
    return render(request, 'zapatillasweb/home.html')

def catalogo_hombre_view(request):
   
    return render(request, 'zapatillasweb/catalogo-hombre.html')

def catalogo_mujer_view(request):
    
    return render(request, 'zapatillasweb/catalogo-mujer.html')

def catalogo_nino_view(request):
  
    return render(request, 'zapatillasweb/catalogo-nino.html')

def contacto_view(request):
    return render(request, 'zapatillasweb/contactos.html')




