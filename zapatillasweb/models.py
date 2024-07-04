from django.db import models


class Zapatilla(models.Model):
    TIPO_CHOICES = [
        ('niño', 'Niño'),
        ('hombre', 'Hombre'),
        ('mujer', 'Mujer'),
    ]
    id_zapatilla = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='images/')
    marca = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

