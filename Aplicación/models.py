from django.db import models

# Modelos para los residuos
class Residuos_agricolas(models.Model):
    cultivo = models.CharField(max_length=100)
    residuo = models.CharField(max_length=100)
    fr = models.FloatField()
    ybas = models.FloatField()
    dr = models.FloatField()
    pci = models.FloatField()
    pb = models.FloatField()
    wf = models.FloatField()

    def __str__(self):
        return self.residuo
    
class Residuos_pecuarios(models.Model):
    animal= models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    pb = models.FloatField()
    pe = models.FloatField()
    dr = models.FloatField()

# Modelo para los rendimientos agricolas  
class Rendimientos_agricolas(models.Model):
    region = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    cultivo = models.CharField(max_length=100)
    rc = models.FloatField()


    def __str__(self):
        return self.departamento
    
# Modelo para producción rsu (personas)
class Produccion_rsu(models.Model):
    region = models.CharField(max_length=100)
    pro_RSU_hab = models.FloatField()
    dr =  models.FloatField()

# Modelo para tipo rsuo
class Tipo_rsuo(models.Model):
    tipo = models.CharField(max_length=100)
    pb = models.FloatField()
    dr =  models.FloatField()

# Modelos para cada Biomasa
class Biomasa_agricola(models.Model):
    residuo_agricola = models.ForeignKey(Residuos_agricolas, on_delete=models.SET_NULL, related_name='residuo_agricola', null=True, blank=True)
    hectareas = models.FloatField(null=True, blank=True)
    rendimiento_agricola = models.ForeignKey(Rendimientos_agricolas, on_delete=models.SET_NULL, related_name='rendimiento_agricola', null=True, blank=True)
    masa_agricola = models.FloatField(null=True, blank=True)
    pot_rt_termo_agri = models.FloatField(null=True, blank=True)
    pot_rt_bioq_agri = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.residuo_agricola.residuo
    
class Biomasa_pecuaria(models.Model):
    residuo_pecuario = models.ForeignKey(Residuos_pecuarios, on_delete=models.SET_NULL, related_name='residuo_pecuario', null=True, blank=True)
    cantidad = models.FloatField(null=True, blank=True)
    masa_pecuaria = models.FloatField(null=True, blank=True)
    pot_rt_bioq_pecu = models.FloatField(null=True, blank=True)

class Biomasa_rsu(models.Model):
    produccion_rsu= models.ForeignKey(Produccion_rsu, on_delete=models.SET_NULL, related_name='produccion_rsu', null=True, blank=True)
    cant_personas = models.PositiveIntegerField(null=True, blank=True)
    masa_RSU = models.FloatField()
    pot_rt_termo_rsu = models.FloatField(null=True, blank=True)

class Biomasa_rsuo(models.Model):
    tipo_rsuo= models.ForeignKey(Tipo_rsuo, on_delete=models.SET_NULL, related_name='tipo_rsuo', null=True, blank=True)
    masa_RSUO = models.FloatField()
    pot_rt_bioq_rsuo = models.FloatField(null=True, blank=True)

# Modelo del proceso en general
class Proceso(models.Model):
    agricola = models.BooleanField(default=False)
    pecuaria = models.BooleanField(default=False)
    rsu = models.BooleanField(default=False)
    rsuo = models.BooleanField(default=False)

    # Viabilidad
    region_choice = (('amazonia','Amazonía'),('orinoquia','Orinoquía'),('pacifica','Pacífica'),)
    region = models.CharField(choices=region_choice, max_length=100, null=True, blank=True)
    distancia = models.FloatField(null=True, blank=True)
    resultado_choice = (('viable','Viable'),('inviable','Inviable'),)
    resultado = models.CharField(choices=resultado_choice, max_length=100, null=True, blank=True)

    # Agricola
    biomasa_agricola = models.ManyToManyField(Biomasa_agricola, related_name='biomasa_agricola', blank=True)
    total_hectareas = models.FloatField(null=True, blank=True, default=0)
    total_masa_agricola = models.FloatField(null=True, blank=True, default=0)
    total_pot_rt_termo_agri = models.FloatField(null=True, blank=True, default=0)
    total_pot_rt_bioq_agri = models.FloatField(null=True, blank=True, default=0)

    masa_agricola_seca = models.FloatField(null=True, blank=True, default=0)
    masa_agricola_humeda = models.FloatField(null=True, blank=True, default=0)

    # Pecuaria
    biomasa_pecuaria =  models.ManyToManyField(Biomasa_pecuaria, related_name='biomasa_pecuaria', blank=True)
    total_cantidad = models.FloatField(null=True, blank=True, default=0)
    total_masa_pecuaria = models.FloatField(null=True, blank=True, default=0)
    total_pot_rt_bioq_pecu = models.FloatField(null=True, blank=True, default=0)

    # RSU
    biomasa_rsu =  models.ManyToManyField(Biomasa_rsu, related_name='biomasa_rsu', blank=True)
    total_masa_rsu = models.FloatField(null=True, blank=True, default=0)
    total_pot_rt_termo_rsu = models.FloatField(null=True, blank=True, default=0)

    # RSUO
    biomasa_rsuo =  models.ManyToManyField(Biomasa_rsuo, related_name='biomasa_rsuo', blank=True)
    total_masa_rsuo = models.FloatField(null=True, blank=True, default=0)
    total_pot_rt_bioq_rsuo = models.FloatField(null=True, blank=True, default=0)

    # Demanda
    ed = models.FloatField(null=True, blank=True, default=0)
    edf = models.FloatField(null=True, blank=True, default=0)
    pot_CGD = models.FloatField(null=True, blank=True, default=0)
    Punit_requerida = models.FloatField(null=True, blank=True, default=0)

    #Resultados
    biomasa_seca = models.FloatField(null=True, blank=True, default=0)
    biomasa_humeda = models.FloatField(null=True, blank=True, default=0)

    rt_final =  models.CharField(max_length=100, null=True, blank=True)

    pot_teo_termo = models.FloatField(null=True, blank=True, default=0)
    pot_teo_termo_unit = models.FloatField(null=True, blank=True, default=0)
    pot_tec_termo_planta = models.FloatField(null=True, blank=True, default=0)
    pot_tec_termo = models.FloatField(null=True, blank=True, default=0)
    cub_rt_termo = models.FloatField(null=True, blank=True, default=0)

    pot_teo_bioq = models.FloatField(null=True, blank=True, default=0)
    pot_teo_bioq_unit = models.FloatField(null=True, blank=True, default=0)
    pot_tec_bioq_planta = models.FloatField(null=True, blank=True, default=0)
    pot_tec_bioq = models.FloatField(null=True, blank=True, default=0)
    cub_rt_bioq = models.FloatField(null=True, blank=True, default=0)

    punit = models.FloatField(null=True, blank=True, default=0)
    tec_final = models.CharField(max_length=100, null=True, blank=True)
    cap_planta = models.FloatField(null=True, blank=True, default=0)
    cant_plantas = models.IntegerField(null=True, blank=True, default=0)
    comentario = models.CharField(max_length=500, null=True, blank=True)

    tipo1 = models.BooleanField(default=False)
    capex1 = models.FloatField(null=True, blank=True, default=0)
    opex1 = models.FloatField(null=True, blank=True, default=0)

    tipo2 = models.BooleanField(default=False)
    capex2 = models.FloatField(null=True, blank=True, default=0)
    opex2 = models.FloatField(null=True, blank=True, default=0)

    tipo3 = models.BooleanField(default=False)
    capex3 = models.FloatField(null=True, blank=True, default=0)
    opex3 = models.FloatField(null=True, blank=True, default=0)

    


