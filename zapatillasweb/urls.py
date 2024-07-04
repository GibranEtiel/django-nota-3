from django.urls import path
from  . import views


urlpatterns = [
    path('home', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('registrar/', views.registrar_view, name='registrar'),
    path('catalogo-hombre/', views.catalogo_hombre_view, name='catalogo-hombre'),
    path('catalogo-mujer/', views.catalogo_mujer_view, name='catalogo-mujer'),
    path('catalogo-nino/', views.catalogo_nino_view, name='catalogo-nino'),
    path('contacto/', views.contacto_view, name='contacto/contactos'),
]

