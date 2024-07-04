from django import forms
from .models import FormularioContacto

class FormularioContacto(forms.ModelForm):
    class Meta:
        model = FormularioContacto
        fields = ['nombre', 'email', 'mensaje']