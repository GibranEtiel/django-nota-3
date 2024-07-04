from django.urls import path
from . import views

from django.conf.urls.static import static

urlpatterns = [
    path('contacto/', views.contacto, name="contactos")
]