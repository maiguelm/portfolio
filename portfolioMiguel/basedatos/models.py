from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.TextField(verbose_name="Titulo")
	descripcion = models.TextField(verbose_name="Descripcion")
	image = models.ImageField(verbose_name="Imagen", upload_to="media")
	url = models.URLField(verbose_name="Link")
 
	def __str__(self):
		return self.title
 
class Meta:
    verbose_name = "basedatos"
    verbose_name_plural = "basesdedatos"
    ordering = ["-created"]