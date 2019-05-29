from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


class Categoria(models.Model):
	nombre = models.CharField(max_length=70, blank=False, null=False)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		db_table = 'categorias'
		verbose_name_plural = 'categorias'


class Novedad(models.Model):
	autor = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
	creada = models.DateTimeField(auto_now_add=True)
	modificada = models.DateTimeField(auto_now=True)
	novedad_categoria = models.ManyToManyField(Categoria)
	titulo = models.CharField(max_length=255, blank=False, null=False)
	contenido = RichTextField()
	enlace = models.URLField(blank=True, null=True)
	slug = models.SlugField(max_length=255, unique=True, editable=False)
	activo = models.BooleanField(default=True)

	class Meta:
		verbose_name_plural = 'novedades'
		db_table = 'novedades'

	def __str__(self):
		return '%s' % (self.titulo)

	def save(self):
		self.slug = slugify(self.titulo)
		super(Novedad, self).save()


class Lugar(models.Model):
	nombre = models.CharField(max_length=255, help_text='salón de uso múltiple')
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s' % (self.nombre)

	class Meta:
		db_table = 'lugares'
		verbose_name_plural = 'lugares'
		ordering = ['nombre']


class Evento(models.Model):
	fecha_inicio = models.DateField('fecha de inicio')
	fecha_fin = models.DateField('fecha de finalización')
	hora_inicio = models.TimeField('horario de comienzo', blank=True, null=True)
	hora_fin = models.TimeField('horario de finalización', blank=True, null=True)
	titulo = models.CharField(max_length=255, blank=False, null=False)
	contenido = RichTextField()
	lugar = models.ForeignKey(Lugar, on_delete=models.CASCADE)
	enlace = models.URLField(blank=True, null=True, help_text='Enlace externo a un sitio web para más información.')
	disertantes = RichTextField(blank=True, null=True)
	autor = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
	slug = models.SlugField(max_length=255, unique=True, editable=False)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s - %s' % (self.titulo, self.fecha_inicio)

	def save(self):
		self.slug = slugify(self.titulo)
		super(Evento, self).save()

	class Meta:
		db_table = 'eventos'
		verbose_name_plural = 'eventos'


class Faq(models.Model):
	titulo = models.CharField(max_length=255)
	respuesta = RichTextField()
	faq_categoria = models.ManyToManyField(Categoria)
	creada = models.DateTimeField(auto_now_add=True)
	modificada = models.DateTimeField(auto_now=True)
	slug = models.SlugField(max_length=255, unique=True, editable=False)
	activo = models.BooleanField(default=True)

	def __str__(self):
		return '%s' % (self.titulo)

	def save(self):
		self.slug = slugify(self.titulo)
		super(Faq, self).save()

	class Meta:
		db_table = 'faq'
		verbose_name_plural = 'preguntas frecuentes'
