from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Zapatilla

def inicio(request):
    zapatillas = Zapatilla.objects.all()  # Obtener todas las zapatillas de la base de datos
    return render(request, 'index.html', {'zapatillas': zapatillas})