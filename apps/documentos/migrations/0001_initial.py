# Generated by Django 2.2.1 on 2019-05-31 05:49

import apps.documentos.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('año', models.IntegerField()),
                ('materia', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('slug', models.SlugField(editable=False, max_length=255)),
                ('archivo', models.FileField(upload_to=apps.documentos.models.Programa._generar_ruta_programa)),
            ],
        ),
    ]
