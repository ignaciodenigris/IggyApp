from django.db import models

# Create your models here.
class Diario(models.Model):
    texto = models.TextField(null=True)
    fecha = models.DateField()  
    def __str__(self):
        return f"Fecha: {self.fecha} texto: {self.texto}"

