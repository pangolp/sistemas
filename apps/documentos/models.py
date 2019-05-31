from django.db import models
from django.template.defaultfilters import slugify
from uuid import uuid4
from datetime import date
import os


class Programa(models.Model):

	def _generar_ruta_programa(instance, filename):
		extension = os.path.splitext(filename)[1][1:]
		filename = os.path.splitext(filename)[0]
		ruta = os.path.join('programas', date.today().strftime('%Y'))
		nombre_archivo = '{}-{}.{}'.format(slugify(filename), date.today().strftime('%Y'), extension)
		return os.path.join(ruta, nombre_archivo)

	año = models.IntegerField()
	materia = models.CharField(max_length=255, blank=False, null=False)
	nombre = models.CharField(max_length=255, blank=False, null=False)
	slug = models.SlugField(max_length=255, editable=False)
	archivo = models.FileField(upload_to=_generar_ruta_programa)

	def __str__(self):
		return '%s' % (self.nombre)

	def save(self):
		self.nombre = self.nombre.lower()
		self.slug = slugify(self.materia)
		super(Programa, self).save()
