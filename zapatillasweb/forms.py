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
    nombreTarjeta = forms.CharField(max_length=100, label='Nombre Completo')
    numeroTarjeta = forms.CharField(label='Número de Tarjeta', widget=forms.TextInput(attrs={'maxlength': '16'}))
    FechaVencimiento = forms.CharField(label='Fecha de Vencimiento (MM/YY)', widget=forms.TextInput(attrs={'maxlength': '5'}))
    Cvv = forms.CharField(max_length=3, label='CVV', widget=forms.TextInput(attrs={'maxlength': '3'}))
    
    def clean_Cvv(self):
        cvv = self.cleaned_data['Cvv']
        if not cvv.isdigit():
            raise forms.ValidationError("El CVV debe contener solo números.")
        return cvv
    