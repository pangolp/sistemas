from django.contrib import admin
from .models import Programa


@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
	list_display = (
		'id',
		'año',
		'nombre',
		'archivo'
	)
