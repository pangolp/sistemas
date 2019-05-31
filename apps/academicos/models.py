from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from apps.usuarios.models import Profesor


class Año(models.Model):
	numero = models.IntegerField(unique=True, primary_key=True)
	observación = RichTextField(blank=True, null=True)

	def __str__(self):
		return '%s' % (self.numero)

	class Meta:
		db_table = 'academico_año'
		verbose_name_plural = 'años'
		ordering = ['numero']


class Materia(models.Model):
	año = models.ForeignKey(Año, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=255, blank=False, null=False, unique=True)
	profesores = models.ManyToManyField(Profesor)
	observación = RichTextField(blank=True, null=True)
	slug = models.SlugField(max_length=255, editable=False)

	def __str__(self):
		return '%s' % (self.nombre)

	def save(self):
		self.slug = slugify(self.nombre)
		super(Materia, self).save()

	class Meta:
		db_table = 'academico_materia'
		verbose_name_plural = 'materias'
		ordering = ['año']
