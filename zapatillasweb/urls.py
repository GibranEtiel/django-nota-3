from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    #base de la pagina
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('catalogo-hombre/', views.catalogo_hombre_view, name='catalogo-hombre'),
    path('catalogo-mujer/', views.catalogo_mujer_view, name='catalogo-mujer'),
    path('catalogo-nino/', views.catalogo_nino_view, name='catalogo-nino'),
    path('contacto/', views.contacto_view, name='contacto/contactos'),
    #login
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name= 'zapatillasweb/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'zapatillasweb/logout.html'), name='logout'),
    #crud
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('listar-producto/', views.listar_productos, name='listar_producto'),
    path('modificar-producto/<id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<id>/', views.eliminar_producto, name='eliminar_producto'),
    
    
]

