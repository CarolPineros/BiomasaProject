# Generated by Django 4.2.2 on 2023-09-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicación', '0010_rename_cap_proceso_cap_serializado'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='cub_total',
            field=models.BooleanField(default=False),
        ),
    ]
