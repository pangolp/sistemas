from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.detail import DetailView
from .models import Novedad


class IndexView(ListView):
	queryset = Novedad.objects.filter(activo=True)
	template_name = 'anuncios/novedad/novedades.html'
	context_object_name = 'novedades'

class NovedadView(DetailView):
	template_name = 'anuncios/novedad/detalle_novedad.html'
	model = Novedad
	context_object_name = 'novedad'
