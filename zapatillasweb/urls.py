from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('home/', views.home, name='home'),
    path('catalogo-hombre/', views.catalogo_hombre_view, name='catalogo-hombre'),
    path('catalogo-mujer/', views.catalogo_mujer_view, name='catalogo-mujer'),
    path('catalogo-nino/', views.catalogo_nino_view, name='catalogo-nino'),
    path('contacto/', views.contacto_view, name='contacto/contactos'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name= 'zapatillasweb/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name= 'zapatillasweb/logout.html'), name='logout'),
    
]

