# Generated by Django 4.2.2 on 2023-09-01 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicación', '0006_proceso_comentario_cantplantas'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='Pot_CGD_parcial_bioq',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='proceso',
            name='Pot_CGD_parcial_termo',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
