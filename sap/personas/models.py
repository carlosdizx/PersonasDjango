from django.db import models


class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f'Perosna {self.id}: {self.nombre} {self.apellido}'
