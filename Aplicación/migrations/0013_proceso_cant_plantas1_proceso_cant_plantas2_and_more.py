# Generated by Django 4.2.2 on 2023-09-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicación', '0012_alter_proceso_cub_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='cant_plantas1',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='proceso',
            name='cant_plantas2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='proceso',
            name='cap_planta1',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='proceso',
            name='cap_planta2',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='proceso',
            name='tec_final1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='proceso',
            name='tec_final2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
