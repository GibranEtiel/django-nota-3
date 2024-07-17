from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import  User
from .models import Zapatilla

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
		help_texts = {k:"" for k in fields }
  
class ZapatillaForm(forms.ModelForm):
    class Meta:
        model = Zapatilla
        fields = '__all__'
        
class CompraForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre Completo')
    direccion = forms.CharField(widget=forms.Textarea, label='Dirección')
    email = forms.EmailField(label='Correo Electrónico')
    telefono = forms.CharField(max_length=15, label='Teléfono')
    cantidad = forms.IntegerField(min_value=1, label='Cantidad')