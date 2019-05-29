from django.contrib import admin
from .models import Categoria, Novedad, Lugar, Evento, Faq


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'nombre',
		'activo'
	)


@admin.register(Novedad)
class NovedadAdmin(admin.ModelAdmin):
	list_display = (
		'autor',
		'creada',
		'modificada',
		'titulo',
		'enlace',
		'activo'
	)


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'nombre',
		'activo'
	)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
	list_display = (
		'fecha_inicio',
		'fecha_fin',
		'hora_inicio',
		'hora_fin',
		'titulo',
		'lugar',
		'enlace',
		'disertantes',
		'autor',
		'activo'
	)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
	list_display = (
		'titulo',
		'creada',
		'modificada',
		'slug',
		'activo'
	)
