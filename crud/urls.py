from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarzapatilla/', views.registrarzapatilla, name='registrarzapatilla'),
    path('editarzapatilla/', views.editarzapatilla),
    path('edicionzapatilla/<nombre>', views.edicionzapatilla, name='edicionzapatilla'),
    path('eliminarzapatilla/<nombre>', views.eliminarzapatilla, name='eliminarzapatilla'),
    
]