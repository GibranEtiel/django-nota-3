from django.shortcuts import render, redirect, get_object_or_404
from .models import Zapatilla
from .forms import UserRegisterForm, ZapatillaForm, CompraForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required


def home(request):
    
    return render(request, 'zapatillasweb/home.html')
def base(request):
    
    return render(request, 'zapatillasweb/base.html')

def contacto_view(request):
    return render(request, 'zapatillasweb/contactos.html')
def cartasp(request):
    return render(request, 'zapatillasweb/cartasp.html')

#registro
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

#Agregar productos
@permission_required('zapatillasweb.add_producto')
def agregar_producto(request):
    data = {
        'form': ZapatillaForm()
    }
    if request.method == 'POST':
        formulario = ZapatillaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            zapatilla = formulario.save()
            messages.success(request, "Zapatilla agregada correctamente")

            # Redirigir según el tipo de zapatilla
        else:
            data["form"] = formulario

    return render(request, 'zapatillasweb/producto/agregar.html', data)

#listar productos
@permission_required('zapatillasweb.view_producto')
def listar_productos(request):
    
    productos = Zapatilla.objects.all()
    page = request.GET.get('page', 1)
    
    try: 
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404
    
    data = {
        'entity' : productos,
        'paginator': paginator
        
        
    }
    return render(request, 'zapatillasweb/producto/listar.html', data)

#editar producto
@permission_required('zapatillasweb.change_producto')
def modificar_producto(request, id):
    
    producto = get_object_or_404(Zapatilla, id=id)
    
    data={
        'form': ZapatillaForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ZapatillaForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Zapatilla modificada correctamente")
            return redirect(to="listar_producto")
        else:
            data["form"] = formulario 
    
    return render(request, 'zapatillasweb/producto/modificar.html', data)
@permission_required('zapatillasweb.delete_producto')
def eliminar_producto(request,id):
    producto = get_object_or_404(Zapatilla,id=id)
    producto.delete()
    messages.success(request,"Zapatilla eliminada correctamente")
    return redirect(to="listar_producto")







#catalogos
def catalogo_hombre(request):
    productos = Zapatilla.objects.filter(tipo='hombre')
    data = {
        'entity': productos
    }
    return render(request, 'zapatillasweb/catalogo-hombre.html', data)

def catalogo_mujer(request):
    productos = Zapatilla.objects.filter(tipo='mujer')
    data = {
        'entity': productos
    }
    return render(request, 'zapatillasweb/catalogo-mujer.html', data)

def catalogo_nino(request):
    productos = Zapatilla.objects.filter(tipo='niño')
    data = {
        'entity': productos
    }
    return render(request, 'zapatillasweb/catalogo-nino.html', data)

#carrito




def compra_producto(request, id):
    producto = get_object_or_404(Zapatilla, id=id)
    form = CompraForm()

    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            messages.success(request, f'¡Compra realizada con éxito!')
            return redirect('home')  # Redirige a la página principal o a donde desees
            
    return render(request, 'zapatillasweb/compra-producto.html', {'form': form, 'producto': producto})

