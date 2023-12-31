# Generated by Django 4.2.2 on 2023-09-07 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biomasa_agricola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hectareas', models.FloatField(blank=True, null=True)),
                ('masa_agricola', models.FloatField(blank=True, null=True)),
                ('pot_rt_termo_agri', models.FloatField(blank=True, null=True)),
                ('pot_rt_bioq_agri', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Biomasa_pecuaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.FloatField(blank=True, null=True)),
                ('masa_pecuaria', models.FloatField(blank=True, null=True)),
                ('pot_rt_bioq_pecu', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Biomasa_rsu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cant_personas', models.PositiveIntegerField(blank=True, null=True)),
                ('masa_RSU', models.FloatField()),
                ('pot_rt_termo_rsu', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Biomasa_rsuo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masa_RSUO', models.FloatField()),
                ('pot_rt_bioq_rsuo', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produccion_rsu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('pro_RSU_hab', models.FloatField()),
                ('dr', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rendimientos_agricolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('cultivo', models.CharField(max_length=100)),
                ('rc', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Residuos_agricolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cultivo', models.CharField(max_length=100)),
                ('residuo', models.CharField(max_length=100)),
                ('fr', models.FloatField()),
                ('ybas', models.FloatField()),
                ('dr', models.FloatField()),
                ('pci', models.FloatField()),
                ('pb', models.FloatField()),
                ('wf', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Residuos_pecuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('pb', models.FloatField()),
                ('pe', models.FloatField()),
                ('dr', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_rsuo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('pb', models.FloatField()),
                ('dr', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agricola', models.BooleanField(default=False)),
                ('pecuaria', models.BooleanField(default=False)),
                ('rsu', models.BooleanField(default=False)),
                ('rsuo', models.BooleanField(default=False)),
                ('region', models.CharField(blank=True, choices=[('amazonia', 'Amazonía'), ('orinoquia', 'Orinoquía'), ('pacifica', 'Pacífica')], max_length=100, null=True)),
                ('distancia', models.FloatField(blank=True, null=True)),
                ('resultado', models.CharField(blank=True, choices=[('viable', 'Viable'), ('inviable', 'Inviable')], max_length=100, null=True)),
                ('total_hectareas', models.FloatField(blank=True, default=0, null=True)),
                ('total_masa_agricola', models.FloatField(blank=True, default=0, null=True)),
                ('total_pot_rt_termo_agri', models.FloatField(blank=True, default=0, null=True)),
                ('total_pot_rt_bioq_agri', models.FloatField(blank=True, default=0, null=True)),
                ('masa_agricola_seca', models.FloatField(blank=True, default=0, null=True)),
                ('masa_agricola_humeda', models.FloatField(blank=True, default=0, null=True)),
                ('total_cantidad', models.FloatField(blank=True, default=0, null=True)),
                ('total_masa_pecuaria', models.FloatField(blank=True, default=0, null=True)),
                ('total_pot_rt_bioq_pecu', models.FloatField(blank=True, default=0, null=True)),
                ('total_masa_rsu', models.FloatField(blank=True, default=0, null=True)),
                ('total_pot_rt_termo_rsu', models.FloatField(blank=True, default=0, null=True)),
                ('total_masa_rsuo', models.FloatField(blank=True, default=0, null=True)),
                ('total_pot_rt_bioq_rsuo', models.FloatField(blank=True, default=0, null=True)),
                ('ed', models.FloatField(blank=True, default=0, null=True)),
                ('edf', models.FloatField(blank=True, default=0, null=True)),
                ('pot_CGD', models.FloatField(blank=True, default=0, null=True)),
                ('Punit_requerida', models.FloatField(blank=True, default=0, null=True)),
                ('comentario_demanda', models.CharField(blank=True, max_length=500, null=True)),
                ('Pot_requerida', models.BooleanField(default=False)),
                ('pot_teo_termo', models.FloatField(blank=True, default=0, null=True)),
                ('pot_teo_termo_unit', models.FloatField(blank=True, default=0, null=True)),
                ('pot_tec_termo_planta', models.FloatField(blank=True, default=0, null=True)),
                ('pot_tec_termo', models.FloatField(blank=True, default=0, null=True)),
                ('cub_rt_termo', models.FloatField(blank=True, default=0, null=True)),
                ('cub_termo100', models.BooleanField(default=False)),
                ('Termoquimica', models.BooleanField(default=False)),
                ('pot_teo_bioq', models.FloatField(blank=True, default=0, null=True)),
                ('pot_teo_bioq_unit', models.FloatField(blank=True, default=0, null=True)),
                ('pot_tec_bioq_planta', models.FloatField(blank=True, default=0, null=True)),
                ('pot_tec_bioq', models.FloatField(blank=True, default=0, null=True)),
                ('cub_rt_bioq', models.FloatField(blank=True, default=0, null=True)),
                ('cub_bioq100', models.BooleanField(default=False)),
                ('Bioquimica', models.BooleanField(default=False)),
                ('Pot_CGD_parcial_bioq', models.FloatField(blank=True, default=0, null=True)),
                ('Pot_CGD_parcial_termo', models.FloatField(blank=True, default=0, null=True)),
                ('Hibrida', models.BooleanField(default=False)),
                ('cub_total', models.FloatField(blank=True, default=0, null=True)),
                ('caso', models.CharField(blank=True, max_length=100, null=True)),
                ('rt_final', models.CharField(blank=True, max_length=100, null=True)),
                ('comentario', models.CharField(blank=True, max_length=500, null=True)),
                ('biomasa_seca', models.FloatField(blank=True, default=0, null=True)),
                ('biomasa_humeda', models.FloatField(blank=True, default=0, null=True)),
                ('punit', models.FloatField(blank=True, default=0, null=True)),
                ('tec_final', models.CharField(blank=True, max_length=100, null=True)),
                ('tec_final1', models.CharField(blank=True, max_length=100, null=True)),
                ('tec_final2', models.CharField(blank=True, max_length=100, null=True)),
                ('cap_planta', models.FloatField(blank=True, default=0, null=True)),
                ('cap_planta1', models.FloatField(blank=True, default=0, null=True)),
                ('cap_planta2', models.FloatField(blank=True, default=0, null=True)),
                ('cant_plantas', models.IntegerField(blank=True, default=0, null=True)),
                ('cant_plantas1', models.IntegerField(blank=True, default=0, null=True)),
                ('cant_plantas2', models.IntegerField(blank=True, default=0, null=True)),
                ('cap_serializado', models.TextField()),
                ('comentario_cantplantas', models.CharField(blank=True, max_length=500, null=True)),
                ('comentario_cubrimiento_planta', models.CharField(blank=True, max_length=500, null=True)),
                ('comentario_cubrimiento_planta1', models.CharField(blank=True, max_length=500, null=True)),
                ('comentario_cubrimiento_planta2', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo1', models.BooleanField(default=False)),
                ('capex1', models.FloatField(blank=True, default=0, null=True)),
                ('opex1', models.FloatField(blank=True, default=0, null=True)),
                ('tipo2', models.BooleanField(default=False)),
                ('capex2', models.FloatField(blank=True, default=0, null=True)),
                ('opex2', models.FloatField(blank=True, default=0, null=True)),
                ('tipo3', models.BooleanField(default=False)),
                ('capex3', models.FloatField(blank=True, default=0, null=True)),
                ('opex3', models.FloatField(blank=True, default=0, null=True)),
                ('biomasa_agricola', models.ManyToManyField(blank=True, related_name='biomasa_agricola', to='Aplicación.biomasa_agricola')),
                ('biomasa_pecuaria', models.ManyToManyField(blank=True, related_name='biomasa_pecuaria', to='Aplicación.biomasa_pecuaria')),
                ('biomasa_rsu', models.ManyToManyField(blank=True, related_name='biomasa_rsu', to='Aplicación.biomasa_rsu')),
                ('biomasa_rsuo', models.ManyToManyField(blank=True, related_name='biomasa_rsuo', to='Aplicación.biomasa_rsuo')),
            ],
        ),
        migrations.AddField(
            model_name='biomasa_rsuo',
            name='tipo_rsuo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tipo_rsuo', to='Aplicación.tipo_rsuo'),
        ),
        migrations.AddField(
            model_name='biomasa_rsu',
            name='produccion_rsu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produccion_rsu', to='Aplicación.produccion_rsu'),
        ),
        migrations.AddField(
            model_name='biomasa_pecuaria',
            name='residuo_pecuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='residuo_pecuario', to='Aplicación.residuos_pecuarios'),
        ),
        migrations.AddField(
            model_name='biomasa_agricola',
            name='rendimiento_agricola',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rendimiento_agricola', to='Aplicación.rendimientos_agricolas'),
        ),
        migrations.AddField(
            model_name='biomasa_agricola',
            name='residuo_agricola',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='residuo_agricola', to='Aplicación.residuos_agricolas'),
        ),
    ]
