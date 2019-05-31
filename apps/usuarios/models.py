from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Cargo(models.Model):
	orden = models.PositiveIntegerField(help_text='Posición en la que se muestra el cargo')
	nombre = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		ordering = ['orden']
		db_table = 'usuario_cargo'
		verbose_name_plural = 'cargos'


class Localidad(models.Model):
	nombre = models.CharField(max_length=255, help_text='Nombre de la localidad', unique=True)

	def __str__(self):
		return '%s' % (self.nombre)


	class Meta:
		ordering = ['nombre']
		db_table = 'localidades'
		verbose_name_plural = 'localidades'


class Provincia(models.Model):
	nombre = models.CharField(max_length=255, help_text='Nombre de la localidad', unique=True)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		ordering = ['nombre']
		db_table = 'provincias'
		verbose_name_plural = 'provincias'


class Persona(models.Model):
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
	provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
	nacimiento = models.DateField(help_text='Fecha de nacimiento')
	observación = RichTextField(blank=True, null=True)
	creado = models.DateTimeField(auto_now_add=True)
	modificado = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True
		ordering = ['-creado']


class Autoridad(Persona):
	cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

	def __str__(self):
		return '%s, %s' % (self.usuario.last_name, self.usuario.first_name)

	class Meta:
		db_table = 'academico_autoridad'
		verbose_name_plural = 'autoridades'


class Profesor(Persona):

	def __str__(self):
		return '%s, %s' % (self.usuario.last_name, self.usuario.first_name)

	class Meta:
		db_table = 'academico_profesor'
		verbose_name_plural = 'profesores'
