from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .forms import *
from .models import *

# Creacion de funcion para vista de home


def introduccion(request):
    context = {}
    return render(request, "introduccion.html", context)


def inicio(request):
    context = {}
    return render(request, "inicio.html", context)


def iniciar_proceso(request):
    proceso = Proceso.objects.create()
    return redirect('viabilidad', proceso.id)


def viabilidad(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        form = ViabilidadForm(request.POST, instance=proceso)
        if form.is_valid():
            form = form.save()
            # Leer R_max de la region
            if form.region == 'amazonia':
                r_max = 27.84
            elif form.region == 'orinoquia':
                r_max = 30.49
            else:
                r_max = 21.28
            # Sabemos si es viable o no
            if form.distancia >= r_max:
                proceso.resultado = 'inviable'
            else:
                proceso.resultado = 'viable'
            # Guardamos los resultados
            proceso.save()
    else:
        form = ViabilidadForm()

    context = {
        'proceso': proceso,
        'form': form,
    }
    return render(request, "viabilidad.html", context)


def agricola_pregunta(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'True':
            proceso.agricola = True
            proceso.save()
            return redirect('agricola', proceso_id)
        else:
            return redirect('pecuaria', proceso_id)
    else:
        messages.error(request, 'No hay respuesta')
        return redirect('agricola', proceso_id)


def agricola(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        form = ResiduosAgricolasForm(request.POST, proceso=proceso)
        if form.is_valid():
            cultivo = form.cleaned_data['cultivo']
            residuo = form.cleaned_data['residuo']
            hectareas = form.cleaned_data['hectareas']
            departamento = form.cleaned_data['departamento']

            residuo_agricola = Residuos_agricolas.objects.get(
                cultivo=cultivo, residuo=residuo)
            fr = residuo_agricola.fr
            ybas = residuo_agricola.ybas
            dr = residuo_agricola.dr
            pci = residuo_agricola.pci
            pb = residuo_agricola.pb
            wf = residuo_agricola.wf

            ac = hectareas

            rendimiento_agricola = Rendimientos_agricolas.objects.get(
                departamento=departamento, cultivo=cultivo)
            rc = rendimiento_agricola.rc

            # Calculo de masa de residuo
            masa_agricola = ac*rc*fr*dr

            # Calculo potencial energia por RT termoquimica
            pot_rt_termo_agri = (masa_agricola*ybas*pci)/3600

            # Calculo potencial energético por RT Bioquimica
            pciMetano = 21600
            pot_rt_bioq_agri = (masa_agricola*pb*pciMetano)/3600

            # Guardar Datos Biomasa Agricola
            biomasa_agricola = Biomasa_agricola.objects.create(
                residuo_agricola=residuo_agricola,
                hectareas=hectareas,
                rendimiento_agricola=rendimiento_agricola,
                masa_agricola=masa_agricola,
                pot_rt_termo_agri=pot_rt_termo_agri,
                pot_rt_bioq_agri=pot_rt_bioq_agri
            )
            biomasa_agricola.save()

            # Calculo de masa agricola humeda o seca

            if wf > 0.5:
                proceso.masa_agricola_humeda += masa_agricola
                proceso.biomasa_humeda += masa_agricola
            else:
                proceso.masa_agricola_seca += masa_agricola
                proceso.biomasa_seca += masa_agricola

            proceso.biomasa_agricola.add(biomasa_agricola)
            proceso.total_hectareas += hectareas
            proceso.total_masa_agricola += masa_agricola
            proceso.total_pot_rt_termo_agri += pot_rt_termo_agri
            proceso.total_pot_rt_bioq_agri += pot_rt_bioq_agri
            proceso.save()
            return redirect('agricola', proceso_id)

    else:
        form = ResiduosAgricolasForm(proceso=proceso)

    context = {
        'proceso': proceso,
        'form': form,
    }
    return render(request, "agricola.html", context)


def pecuaria_pregunta(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'True':
            proceso.pecuaria = True
            proceso.save()
            return redirect('pecuaria', proceso_id)
        else:
            return redirect('rsu', proceso_id)
    else:
        messages.error(request, 'No hay respuesta')
        return redirect('pecuaria', proceso_id)


def pecuaria(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        form = ResiduosPecuariosForm(request.POST)
        if form.is_valid():
            animal = form.cleaned_data['animal']
            tipo = form.cleaned_data['tipo']
            cantidad = form.cleaned_data['cantidad']

            residuo_pecuario = Residuos_pecuarios.objects.get(
                animal=animal, tipo=tipo)
            pb = residuo_pecuario.pb
            pe = residuo_pecuario.pe
            dr = residuo_pecuario.dr

            cant_animal = cantidad

            # Calculo de masa de residuo
            masa_pecuaria = (cant_animal*pe*dr*365)/1000

            # Calculo potencial energético por RT Bioquimica
            pciMetano = 21600
            pot_rt_bioq_pecu = (masa_pecuaria*pb*pciMetano)/3600

            # Guardar Datos Biomasa Pecuaria
            biomasa_pecuaria = Biomasa_pecuaria.objects.create(
                residuo_pecuario=residuo_pecuario,
                cantidad=cantidad,
                masa_pecuaria=masa_pecuaria,
                pot_rt_bioq_pecu=pot_rt_bioq_pecu
            )
            biomasa_pecuaria.save()

            proceso.biomasa_humeda += masa_pecuaria
            proceso.biomasa_pecuaria.add(biomasa_pecuaria)
            proceso.total_cantidad += cantidad
            proceso.total_masa_pecuaria += masa_pecuaria
            proceso.total_pot_rt_bioq_pecu += pot_rt_bioq_pecu
            proceso.save()

            return redirect('pecuaria', proceso_id)

    else:
        form = ResiduosPecuariosForm()

    context = {
        'proceso': proceso,
        'form': form,
    }
    return render(request, "pecuaria.html", context)


def rsu_pregunta(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        print(respuesta)
        if respuesta == 'True':
            proceso.rsu = True
            proceso.save()
            return redirect('rsu', proceso_id)
        else:
            return redirect('rsuo', proceso_id)
    else:
        print("Depurador: ejecicion no valido")
        return redirect('rsu', proceso_id)


def rsu(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        form1 = CantidadRSUFrom(request.POST)
        form2 = ResiduosRSUForm(request.POST)
        if form1.is_valid():
            cant_personas = form1.cleaned_data['cant_personas']
            region = form1.cleaned_data['region']

            produccion_rsu = Produccion_rsu.objects.get(region=region)
            pro_RSU_hab = produccion_rsu.pro_RSU_hab
            dr = produccion_rsu.dr
            masa_RSU = (cant_personas*dr*pro_RSU_hab*365)/1000

            biomasa_rsu = Biomasa_rsu.objects.create(
                produccion_rsu=produccion_rsu,
                cant_personas=cant_personas,
                masa_RSU=masa_RSU,
            )

        elif form2.is_valid():
            masa_RSU = form2.cleaned_data['masa_RSU']

            biomasa_rsu = Biomasa_rsu.objects.create(
                masa_RSU=masa_RSU,
            )

        else:
            masa_RSU = None

        if masa_RSU is not None:
            PCI_prom_RSU = 10694.1
            pot_rt_termo_rsu = (PCI_prom_RSU*masa_RSU*0.582)/3600

            biomasa_rsu.pot_rt_termo_rsu = pot_rt_termo_rsu
            biomasa_rsu.save()

            proceso.biomasa_seca += proceso.masa_agricola_seca + masa_RSU
            proceso.biomasa_rsu.add(biomasa_rsu)
            proceso.total_masa_rsu += masa_RSU
            proceso.total_pot_rt_termo_rsu += pot_rt_termo_rsu
            proceso.save()

        return redirect('rsu', proceso_id)
    else:
        form1 = CantidadRSUFrom()
        form2 = ResiduosRSUForm()

    context = {
        'proceso': proceso,
        'form1': form1,
        'form2': form2,
    }
    return render(request, "rsu.html", context)


def rsuo_pregunta(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        respuesta = request.POST.get('respuesta')
        if respuesta == 'True':
            proceso.rsuo = True
            proceso.save()
            return redirect('rsuo', proceso_id)
        else:
            return redirect('demanda', proceso_id)
    else:
        messages.error(request, 'No hay respuesta')
        return redirect('rsu', proceso_id)


def rsuo(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        form = ResiduosRSUOForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            masa_RSUO = form.cleaned_data['masa_RSUO']

            tipo_rsuo = Tipo_rsuo.objects.get(tipo=tipo)
            pb = tipo_rsuo.pb
            dr = tipo_rsuo.dr

            PCImetano = 21600
            pot_rt_bioq_rsuo = (pb*dr*PCImetano*masa_RSUO)/3600

            biomasa_rsuo = Biomasa_rsuo.objects.create(
                tipo_rsuo=tipo_rsuo,
                masa_RSUO=masa_RSUO,
                pot_rt_bioq_rsuo=pot_rt_bioq_rsuo,
            )

            proceso.biomasa_humeda += masa_RSUO
            proceso.biomasa_rsuo.add(biomasa_rsuo)
            proceso.total_masa_rsuo += masa_RSUO
            proceso.total_pot_rt_bioq_rsuo += pot_rt_bioq_rsuo
            proceso.save()

            return redirect('rsuo', proceso_id)
        else:
            print("Depurador: ejecicion no valido")
    else:
        form = ResiduosRSUOForm()

    context = {
        'proceso': proceso,
        'form': form,
    }
    return render(request, "rsuo.html", context)


def demanda(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)
    if request.method == 'POST':
        form1 = CantidadDemandaForm(request.POST)
        form2 = DemandaForm(request.POST)
        if form1.is_valid():
            cant_hab = form1.cleaned_data['cant_hab']
            consumo_per_capital = (1492.5)/1000.0
            ed = round(cant_hab * consumo_per_capital, 2)
        elif form2.is_valid():
            ed = form2.cleaned_data['ed']
        else:
            ed = None

        if ed is not None:

            edf = ed + ed * (0.3)
            pot_CGD = round((ed/365) / (24*0.6), 2)
            Punit_requerida = round(pot_CGD/2, 2)

            proceso.ed = ed
            proceso.edf = edf
            proceso.pot_CGD = pot_CGD
            proceso.Punit_requerida = Punit_requerida
            proceso.save()

        return redirect('demanda', proceso_id)
    else:
        form1 = CantidadDemandaForm()
        form2 = DemandaForm()

    context = {
        'proceso': proceso,
        'form1': form1,
        'form2': form2,
    }
    return render(request, "demanda.html", context)


def capacidad_y_cantidad_plantas(proceso, cap, punit):
    for i in cap:
        if punit/i > 1:
            proceso.cap_planta = i
            if (punit/i)-int(punit/i) < 0.5:
                proceso.cant_plantas = int(punit/i)
            else:
                proceso.cant_plantas = int(punit/i) + 1
            break
        else:
            pass


def resultados(request, proceso_id):
    proceso = Proceso.objects.get(id=proceso_id)

    if proceso.biomasa_seca >= proceso.biomasa_humeda:
        proceso.rt_final = 'Termoquimica'
        pot_teo_termo = proceso.total_pot_rt_termo_agri + proceso.total_pot_rt_termo_rsu
        pot_teo_termo_unit = pot_teo_termo/(8760*0.6)

        proceso.pot_teo_termo = pot_teo_termo
        proceso.pot_teo_termo_unit = pot_teo_termo_unit

        if pot_teo_termo_unit > 3:
            eficiencia = 0.26
        else:
            eficiencia = 0.22

        pot_tec_termo = pot_teo_termo*eficiencia
        pot_tec_termo_planta = pot_teo_termo_unit*eficiencia

        proceso.pot_tec_termo_planta = pot_tec_termo_planta

        proceso.pot_tec_termo = pot_tec_termo

        cub_rt_termo = (pot_tec_termo/proceso.edf)*100
        cub_rt_termo = round(cub_rt_termo, 2)

        proceso.cub_rt_termo = cub_rt_termo

        if pot_tec_termo != 0:  # agregue esta funcion por que salia el error division entre cero - CarolP
            if (proceso.edf/pot_tec_termo) > 1:
                proceso.comentario = (
                    f'No es posible cubrir el 100% de la demanda con la biomasa disponible. Cubre el {cub_rt_termo}% de la demanda energética, el faltante se debe cubrir con otra fuente distinta a la Biomasa residual ingresada.')
                if cub_rt_termo < 50:
                    punit = pot_tec_termo_planta
                else:
                    punit = pot_tec_termo_planta/2
            else:
                proceso.comentario = (
                    f'Si es posible cubrir el 100% de la demanda energética con la biomasa disponible.')
                punit = proceso.Punit_requerida

            proceso.punit = punit
        else:
            proceso.comentario = (
                f'No es posible cubrir el 100% de la demanda con la biomasa disponible. Cubre el {cub_rt_termo}% de la demanda energética, el faltante se debe cubrir con otra fuente distinta a la Biomasa residual ingresada.')
        # Tecnologia sugeriada segun Capacidad
        if punit >= 10:
            proceso.tec_final = 'Combustión - Ciclo Rankine Convencional accionado con turbuna accial o gasificación'
            proceso.tipo1 = True
            proceso.tipo2 = True
            cap = [50, 40, 30, 20, 10]
            capacidad_y_cantidad_plantas(proceso, cap, punit)
        elif punit >= 3:
            proceso.tec_final = 'Combustión - Ciclo Rankine Convencional accionado con turbuna accial'
            proceso.tipo1 = True
            cap = [3, 5, 10]
            capacidad_y_cantidad_plantas(proceso, cap, punit)
        elif punit >= 0.01:
            proceso.tec_final = 'Combustión - Ciclo Rankine Orgánico'
            proceso.tipo1 = True
            cap = [2.5, 2, 1, 0.5, 0.45, 0.4, 0.35,
                   0.3, 0.2, 0.1, 0.05, 0.04, 0.01]
            capacidad_y_cantidad_plantas(proceso, cap, punit)
        else:
            proceso.tec_final = 'No es viable el Proyecto'
    else:
        proceso.rt_final = 'Bioquimica'
        pot_teo_bioq = proceso.total_pot_rt_bioq_agri + \
            proceso.total_pot_rt_bioq_pecu + proceso.total_pot_rt_bioq_rsuo
        pot_teo_bioq_unit = pot_teo_bioq/(8760*0.6)

        proceso.pot_teo_bioq = pot_teo_bioq
        proceso.pot_teo_bioq_unit = pot_teo_bioq_unit

        if pot_teo_bioq_unit > 3:
            eficiencia = 0.26
        else:
            eficiencia = 0.22

        pot_tec_bioq = pot_teo_bioq*eficiencia
        pot_tec_bioq_planta = pot_teo_bioq_unit*eficiencia

        proceso.pot_tec_bioq_planta = pot_tec_bioq_planta
        proceso.pot_tec_bioq = pot_tec_bioq

        cub_rt_bioq = (pot_tec_bioq/proceso.edf)*100
        cub_rt_bioq = round(cub_rt_bioq, 2)

        proceso.cub_rt_bioq = cub_rt_bioq

        if (proceso.edf/pot_tec_bioq) > 1:
            proceso.comentario = (
                f'No es posible cubrir el 100% de la demanda con la biomasa disponible. Cubre el {cub_rt_bioq}% de la demanda energética, el faltante se debe cubrir con otra fuente distinta a la Biomasa residual ingresada.')
            if cub_rt_bioq < 0.5:
                punit = pot_tec_bioq_planta
            else:
                punit = pot_tec_bioq_planta/2
        else:
            proceso.comentario = (
                f'Si es posible cubrir el 100% de la demanda energética con la biomasa disponible.')
            punit = proceso.Punit_requerida

        proceso.punit = punit

        # Tecnologia sugeriada segun Capacidad
        if punit >= 0.1:
            proceso.tec_final = 'Digestión anaerobia con motor de combustión interna'
            proceso.tipo3 = True
            cap = [1, 0.8, 0.5, 0.3, 0.1]
            capacidad_y_cantidad_plantas(proceso, cap, punit)
        else:
            proceso.tec_final = 'No es viable el proyecto, Opta por usar BR para otros fines'

    # Estimacion de costos
    if proceso.tipo1:
        proceso.capex1 = 2706378 * \
            (proceso.total_masa_agricola + proceso.total_masa_rsu)
        proceso.opex1 = 513922 * \
            (proceso.total_masa_agricola + proceso.total_masa_rsu)

    if proceso.tipo2:
        proceso.capex2 = 5060471 * \
            (proceso.total_masa_agricola + proceso.total_masa_rsu)
        proceso.opex2 = 2615198 * \
            (proceso.total_masa_agricola + proceso.total_masa_rsu)

    if proceso.tipo3:
        proceso.capex3 = 857917 * \
            (proceso.total_masa_pecuaria + proceso.total_masa_rsuo)
        proceso.opex3 = 215515 * \
            (proceso.total_masa_pecuaria + proceso.total_masa_rsuo)

    # Guardamos los resultados
    proceso.save()

    context = {
        'proceso': proceso,
    }
    return render(request, "resultados.html", context)
