from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    dia_publicacion = models.DateField()
    cantidad_videos = models.IntegerField()
    imagen = models.ImageField(upload_to='cursos_imagenes/', null=True, blank=True)

    def __str__(self):
        return self.nombre