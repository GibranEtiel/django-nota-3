# contacto/views.py
from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.urls import reverse

def contacto(request):
    formulario_contacto = FormularioContacto()  # Inicializar formulario vacío

    if request.method == "POST":
        formulario_contacto = FormularioContacto(request.POST)  # Bind datos POST al formulario

        if formulario_contacto.is_valid():
            nombre = formulario_contacto.cleaned_data.get("nombre")
            email = formulario_contacto.cleaned_data.get("email")
            contenido = formulario_contacto.cleaned_data.get("mensaje")

            email = EmailMessage(
                "Mensaje desde App Django",
                f"El usuario con nombre {nombre} con la dirección {email} escribe lo siguiente:\n\n {contenido}",
                "",
                ["nicolas.programador@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                return redirect(reverse('contactos') + '?valido')  # Redirigir usando el nombre de la URL
            except:
                return redirect(reverse('contactos') + '?no-valido')  # Redirigir usando el nombre de la URL

    return render(request, "contacto/contactos.html", {
        "miFormulario": formulario_contacto,
    })
