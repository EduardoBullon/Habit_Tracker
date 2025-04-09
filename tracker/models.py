from django.db import models
from django.contrib.auth.models import User

class Hábito(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    frecuencia = models.CharField(max_length=20, choices=[('diario', 'Diario'), ('semanal', 'Semanal')])

    def __str__(self):
        return self.nombre

class RegistroHábito(models.Model):
    hábito = models.ForeignKey(Hábito, related_name='registros', on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    completado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hábito.nombre} - {self.fecha} - {'Completado' if self.completado else 'Pendiente'}"
