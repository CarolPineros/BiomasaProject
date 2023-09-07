import math

Cap=[0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]

punit = round(float(input("Ingresar punit: ")), 2)
pot_CGD = round(float(input("Ingresar POT_CGD: ")), 2)

found_solution = False

for i in Cap:
    if punit/i >= 1:
        Cant_plantas_1 = int(pot_CGD/i)
        MW_ofrecido = Cant_plantas_1 * i
        MW_faltante = round(MW_ofrecido - pot_CGD, 2)

        if MW_faltante > 0:
            comentario_cubrimiento_planta = f'{MW_faltante} MW sin cubrimiento por la capacidad de planta, puede cubrir con otra planta de capacidad disponible'
            comentario_cantplantas = f'Número de plantas: {Cant_plantas_1}, Potencia: {i} MW'

            print(comentario_cantplantas)
            print(comentario_cubrimiento_planta)
            found_solution = True
            break

if not found_solution:
    print("No se encontró una solución con las capacidades de planta disponibles.")