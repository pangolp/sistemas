# Generated by Django 2.2.1 on 2019-05-31 05:49

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'categorias',
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='salón de uso múltiple', max_length=255)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'lugares',
                'db_table': 'lugares',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Novedad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creada', models.DateTimeField(auto_now_add=True)),
                ('modificada', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('enlace', models.URLField(blank=True, null=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('novedad_categoria', models.ManyToManyField(to='anuncios.Categoria')),
            ],
            options={
                'verbose_name_plural': 'novedades',
                'db_table': 'novedades',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('respuesta', ckeditor.fields.RichTextField()),
                ('creada', models.DateTimeField(auto_now_add=True)),
                ('modificada', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('faq_categoria', models.ManyToManyField(to='anuncios.Categoria')),
            ],
            options={
                'verbose_name_plural': 'preguntas frecuentes',
                'db_table': 'faq',
            },
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='fecha de inicio')),
                ('fecha_fin', models.DateField(verbose_name='fecha de finalización')),
                ('hora_inicio', models.TimeField(blank=True, null=True, verbose_name='horario de comienzo')),
                ('hora_fin', models.TimeField(blank=True, null=True, verbose_name='horario de finalización')),
                ('titulo', models.CharField(max_length=255)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('enlace', models.URLField(blank=True, help_text='Enlace externo a un sitio web para más información.', null=True)),
                ('disertantes', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anuncios.Lugar')),
            ],
            options={
                'verbose_name_plural': 'eventos',
                'db_table': 'eventos',
            },
        ),
    ]