from django.shortcuts import render, redirect
from .models import Zapatilla

# Vista para mostrar el listado de zapatillas
def home(request):
    zapatillas_listado = Zapatilla.objects.all()
    return render(request, "gestionzapatillas.html", {"zapatillas": zapatillas_listado})




# Vista para registrar una nueva zapatilla
def registrarzapatilla(request):
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        tipo = request.POST['tipo']
        precio = request.POST['numPrecio']
        stock = request.POST['numStock']
        imagen = request.FILES['fileImagen']
        marca = request.POST['txtMarca']

        zapatilla = Zapatilla.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            tipo=tipo,
            precio=precio,
            stock=stock,
            imagen=imagen,
            marca=marca
        )
        
        return redirect('/')

def edicionzapatilla(request,nombre):
 zapatilla = Zapatilla.objects.get(nombre=nombre) 
 return render(request, "edicionzapatilla.html", {"zapatillas":zapatilla})   
    
def editarzapatilla(request):
        
        nombre = request.POST['txtNombre']
        descripcion = request.POST['txtDescripcion']
        tipo = request.POST['tipo']
        precio = request.POST['numPrecio']
        stock = request.POST['numStock']
        imagen = request.FILES['fileImagen']
        marca = request.POST['txtMarca']

        zapatilla = Zapatilla.objects.get(nombre=nombre) 
        zapatilla.nombre=nombre,
        zapatilla.descripcion=descripcion,
        zapatilla.tipo=tipo,
        zapatilla.precio=precio,
        zapatilla.stock=stock,
        zapatilla.imagen=imagen,
        zapatilla.marca=marca
        zapatilla.save()
        return redirect('/')

def eliminarzapatilla(request,nombre):
      zapatilla = Zapatilla.objects.get(nombre=nombre)
      zapatilla.delete()
      return redirect('/')