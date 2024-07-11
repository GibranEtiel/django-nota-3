from django.shortcuts import render, redirect 
from .models import Zapatilla
from .forms import UserRegisterForm
from django.contrib import messages

def index(request):
    return render(request, 'zapatillasweb/index.html')

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

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if  form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = {'form' : form }
            
    return render(request, 'zapatillasweb/register.html', context )







