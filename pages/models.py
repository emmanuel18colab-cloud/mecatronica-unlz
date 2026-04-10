from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Post(models.Model):
    TIPO_CHOICES = [
        ('apunte', 'Apunte'),
        ('parcial', 'Parcial resuelto'),
        ('clase', 'Clase particular'),
        ('noticia', 'Noticia'),
        ('proyecto', 'Proyecto'),
        ('link', 'Link de WhatsApp'),
    ]

    ANIO_CHOICES = [
        ('1', '1er año'),
        ('2', '2do año'),
        ('3', '3er año'),
        ('4', '4to año'),
        ('5', '5to año'),
    ]

    titulo = models.CharField(max_length=200)
    materia = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='apunte')
    anio = models.CharField(max_length=1, choices=ANIO_CHOICES, default='1')
    contenido = RichTextField()
    imagen = models.ImageField(upload_to='posts/', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha']
