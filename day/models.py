from django.db import models

# Create your models here.

class Day(models.Model):
    ejercicio = models.BooleanField(default=False)
    c = models.BooleanField(default=False)
    python = models.BooleanField(default=False)
    ingles = models.BooleanField(default=False)
    libro = models.BooleanField(default=False)
    dia = models.DateTimeField(auto_created=True)

    def __str__(self):
        dia_formateado = self.dia.strftime('%d-%m-%Y') 
        return str(self.id) + "- " + dia_formateado