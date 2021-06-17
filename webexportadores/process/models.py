from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Process(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="process_bg")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de edicion")
    author = models.ForeignKey(
        User, verbose_name="Autor", on_delete=models.PROTECT, blank=True, null=True)
    active = models.BooleanField(verbose_name="Activo", blank=True, null=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)

    class Meta:
        verbose_name = "Process"
        verbose_name_plural = "Process"
        ordering = ["order"]

    def __str__(self):
        return self.title
