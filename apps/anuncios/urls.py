from django.urls import path
from .views import (
	IndexView,
	NovedadView,
)


app_name = 'anuncios'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
