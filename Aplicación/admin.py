from django.contrib import admin
from .models import *


class ProcesoAdmin(admin.ModelAdmin):
    list_display = ('id','region','distancia','resultado')
    list_display_links = ('id','region',)

class Residios_agricolasAdmin(admin.ModelAdmin):
    list_display = ('id','cultivo','residuo','fr','ybas','dr','pci','pb')
    list_display_links = ('id','cultivo',)

class Residios_pecuariosAdmin(admin.ModelAdmin):
    list_display = ('id','animal','tipo','pb','pe','dr')
    list_display_links = ('id','animal',)

class Rendimientos_agricolasAdmin(admin.ModelAdmin):
    list_display = ('id','region','departamento','cultivo','rc')
    list_display_links = ('id','region',)

class Produccion_rsuAdmin(admin.ModelAdmin):
    list_display = ('id','region','pro_RSU_hab','dr')
    list_display_links = ('id','region',)

class Tipo_rsuoAdmin(admin.ModelAdmin):
    list_display = ('id','tipo','pb','dr')
    list_display_links = ('id','tipo',)

class Biomasa_agricolaAdmin(admin.ModelAdmin):
    list_display = ('id','residuo_agricola','hectareas','rendimiento_agricola','masa_agricola','pot_rt_termo_agri','pot_rt_bioq_agri')
    list_display_links = ('id','residuo_agricola',)

class Biomasa_pecuariaAdmin(admin.ModelAdmin):
    list_display = ('id','residuo_pecuario','cantidad','masa_pecuaria','pot_rt_bioq_pecu')
    list_display_links = ('id','residuo_pecuario',)

class Biomasa_rsuAdmin(admin.ModelAdmin):
    list_display = ('id','cant_personas','masa_RSU')
    list_display_links = ('id','cant_personas',)


# Register your models here.
admin.site.register(Proceso, ProcesoAdmin)
admin.site.register(Residuos_agricolas, Residios_agricolasAdmin)
admin.site.register(Residuos_pecuarios, Residios_pecuariosAdmin)
admin.site.register(Rendimientos_agricolas, Rendimientos_agricolasAdmin)
admin.site.register(Produccion_rsu, Produccion_rsuAdmin)
admin.site.register(Tipo_rsuo, Tipo_rsuoAdmin)
admin.site.register(Biomasa_agricola, Biomasa_agricolaAdmin)
admin.site.register(Biomasa_pecuaria, Biomasa_pecuariaAdmin)
admin.site.register(Biomasa_rsu, Biomasa_rsuAdmin)