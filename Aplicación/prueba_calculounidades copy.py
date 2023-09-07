import math
#Cap=(1.0, 0.95, 0.9, 0.85, 0.8, 0.75, 0.7, 0.65, 0.6, 0.55, 0.5, 0.45, 0.4, 0.35, 0.3, 0.25, 0.2, 0.15, 0.1)
Cap=(0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0)
punit=float(input("IngreSar punit"))
pot_CGD=float(input("ingresar POT_CGD"))

for i in Cap:
    if i>=punit:
    #if punit/i >=1:
        if (pot_CGD/i)-int(pot_CGD/i) <0.5:
            Cant_plantas_1=int(pot_CGD/i)
  
      
        else:
            Cant_plantas_1=int(pot_CGD/i)+1
        MW_ofrecido=Cant_plantas_1*i
        MW_faltante = round(MW_ofrecido-pot_CGD,2)
       
        if MW_faltante >=0:
            cant_plantas=Cant_plantas_1
            comentario_cantplantas= ("No plantas:",Cant_plantas_1,"Potencia:",i, "MW")
            comentario_cubrimiento_planta= ("Cubre total de demanda energética")
            print(comentario_cantplantas)  
            print(comentario_cubrimiento_planta)    



            

        else:
            pass

            


    else:
        pass
        #print("Ninguna capacidad es valida")

