from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    active = models.BooleanField(verbose_name="Activa",blank=True, null=True)

    class Meta:
        verbose_name="categoria"
        verbose_name_plural ="categorias"
        ordering = ["-created"] #ordernacion de mas reciente a mas viejo

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    intro =  models.CharField(max_length=200, verbose_name="Introduccion",blank=True, null=True)
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen",upload_to="Posts")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.PROTECT, blank=True, null=True)
    categories = models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_posts")
    active = models.BooleanField(verbose_name="Activo",blank=True, null=True)

    class Meta:
        verbose_name="post"
        verbose_name_plural ="posts"
        ordering = ["-created"] #ordernacion de mas reciente a mas viejo

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Conenido")
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")


    class Meta:
        verbose_name="blog"
        verbose_name_plural ="blogs"
        ordering = ["-created"] #ordernacion de mas reciente a mas viejo

    def __str__(self):
        return self.title
