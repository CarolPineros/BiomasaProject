# Generated by Django 4.2.2 on 2023-09-03 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicación', '0013_proceso_cant_plantas1_proceso_cant_plantas2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='comentario_cubrimiento_planta1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='proceso',
            name='comentario_cubrimiento_planta2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
