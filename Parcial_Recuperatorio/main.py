#Nombre y Apellido: Junior Camacho 
#Div: 117

from paquetes.matriz import *
from paquetes.funcion_1 import *


#ubicaciones
areas = ["Rosario","Cordoba","Salta","Bahia Blanca"]
aparatos_tegnologico = ["Arduino UNO", "Sensor de temperatura","Cable USB","Display LCD","Protoboard"]


menu = True

        #Arduino UNO, Sensor de temperatura,  Cable USB,  Display LCD, Protoboard
matriz_precio = [[120, 100, 100, 312, 2343],#Rosario
                 [1200, 800, 100, 312, 234],#Cordoba
                 [120, 100, 10000, 312, 234],#Salta
                 [120, 100, 100,  3124, 2504]]#Bahia Blanca




while menu:

    print("")

    opcion = int(input("Ingrese una opcion:"))

    match opcion:
        case 1:
            print("selecciones 1: \n")
            matriz_precio = inicialisaar_matriz(len(areas), 
                                         len(aparatos_tegnologico))
            
            matriz_precio = cargar_matriz_secuencial(matriz_precio)

            for i in range(len(matriz_precio)):
                for j in range(len(matriz_precio[i])):
                    print(matriz_precio[i][j], end = " ")
                print("")

        case 2:
            print("selecciones 2:Mostrar depósitos con stock total superior a 5000 unidades \n")

            mostrar_depositos_mayor_5000(matriz_precio, areas)# -> Depósitos

        case 3:
            print("selecciones 3:Mostrar insumos con stock total superior a 3000 unidades \n")

            mostrar_insumos_con_stock_superior(matriz_precio, aparatos_tegnologico, 3000) # | Insumos
                                                                                          # v

                

        case 4:
            print("selecciones 4:Identificar el depósito con mayor cantidad de unidades por insumo \n")

            # 4. Identificar el depósito con mayor cantidad de unidades por insumo
            # Para cada tipo de insumo, determinar en cuál de los cuatro depósitos se encuentra la mayor cantidad
            # almacenada. Mostrar tanto el nombre del insumo como el depósito correspondiente.


            for j in range(len(aparatos_tegnologico)):  # Recorremos columnas = insumos
                mayor = -1
                indice_mayor = -1
                for i in range(len(areas)):  # Recorremos filas = depósitos
                    if matriz_precio[i][j] > mayor:
                        mayor = matriz_precio[i][j]
                        indice_mayor = i
                print(f"Insumo: {aparatos_tegnologico[j]} - Depósito: {areas[indice_mayor]} - Unidades: {mayor}")

        case 5:
            print("selecciones 5:")


        case 6:
            print("selecciones 6:")

            totales = []
            for i in range(len(matriz_precio)):
                suma = 0
                for j in range(len(matriz_precio[i])):
                    suma = suma + matriz_precio[i][j]
                totales = totales + [suma]

            for i in range(len(totales)):
                for j in range(0, len(totales) - i - 1):
                    if totales[j] < totales[j + 1]:
                        
                        aux_total = totales[j]
                        totales[j] = totales[j + 1]
                        totales[j + 1] = aux_total

                        
                        aux_area = areas[j]
                        areas[j] = areas[j + 1]
                        areas[j + 1] = aux_area

        
            for i in range(len(totales)):
                print(f"Depósito: {areas[i]} - Total ventas: {totales[i]} unidades")

                    

        case 7:
            print("selecciones 7:")
        case 8:
            print("selecciones 8:")
        case 9:
            print("selecciones 9:")
        case 10:
            print("Salida")
            ejecutar_menu = False

            break
        
        case _:
            pass



 # Concepto	            En la matriz	    Lista relacionada
# Depósitos	            Filas (i)	            areas
# Insumos/productos	    Columnas (j)	    aparatos_tegnologico





#####################################################################################################################################




# while menu:

#     print("")

#     opcion = int(input("Ingrese una opcion:"))

#     match opcion:
#         case 1:
#             print("selecciones 1:")
#             matriz_precio = inicialisaar_matriz(len(areas), 
#                                          len(aparatos_tegnologico))
            
#             matriz_precio = cargar_matriz_secuencial(matriz_precio)

#             for i in range(len(matriz_precio)):
#                 for j in range(len(matriz_precio[i])):
#                     print(matriz_precio[i][j],end = " ")
#                 print("")

#         case 2:
#             print("selecciones 2:Mostrar depósitos con stock total superior a 5000 unidades")

#             for i in range(len(matriz_precio)):
#                 total = 0
#                 for j in range(len(matriz_precio[i])):
#                     total = total + matriz_precio[i][j]
#                 if total > 5000:
#                     print(f"Depósito:{areas[i]}  Stock total: {total}")

#         case 3:
#             print("selecciones 3:Mostrar insumos con stock total superior a 3000 unidades")

#             for j in range(len(aparatos_tegnologico)):
#                 total = 0

#                 for i in range(len(areas)):  
#                     total = total + matriz_precio[i][j]

#                 if total > 3000:
#                     print(f"El insumo '{aparatos_tegnologico[j]}' tiene un stock total de {total} unidades.")


#         case 4:
#             print("selecciones 4:Identificar el depósito con mayor cantidad de unidades por insumo")

#             # 4. Identificar el depósito con mayor cantidad de unidades por insumo
#             # Para cada tipo de insumo, determinar en cuál de los cuatro depósitos se encuentra la mayor cantidad
#             # almacenada. Mostrar tanto el nombre del insumo como el depósito correspondiente.

#             for j in range(len(aparatos_tegnologico)): 
#                 maximo = matriz_precio[0][j]
#                 indice_max = 0

#                 for i in range(1, len(areas)): 
#                     if matriz_precio[i][j] > maximo:
#                         maximo = matriz_precio[i][j]
#                         indice_max = i

#                 print(f"El insumo '{aparatos_tegnologico[j]}' tiene más stock en '{areas[indice_max]}' con {maximo} unidades.")

#                 # Concepto	            En la matriz	    Lista relacionada
#                 # Depósitos	            Filas (i)	            areas
#                 # Insumos/productos	    Columnas (j)	    aparatos_tegnologico


#         case 5:
#             print("selecciones 5:")


#         case 6:
#             print("selecciones 6:")

#             # 6. Informe de ventas por depósito (ordenado)
#             # Calcular el total vendido por depósito sumando todos los insumos. Ordenar los resultados de
#             # mayor a menor utilizando el algoritmo Bubble Sort, e informar el total de ventas de cada depósito.

#             oredenamiento = ordenar_burbujeo(matriz_precio)

#             for i in range(len(matriz_precio)):#
#                 ordenar_burbujeo(matriz_precio[i])

#             for i in range(len(oredenamiento)):
#                 for j in range(len(oredenamiento[i])):
#                     print(oredenamiento[i][j],end = " ")
#                 print("")

        

#         case 7:
#             print("selecciones 7:")
#         case 8:
#             print("selecciones 8:")
#         case 9:
#             print("selecciones 9:")
#         case 10:
#             print("Salida")
#             ejecutar_menu = False

#             break
        
#         case _:
#             pass


# ###############################################################################################################################

# #Nombre y Apellido: Junior Camacho 
# #Div: 117

# from paquetes.matriz import *

# #ubicaciones
# areas = ["Rosario","Cordoba","Salta","Bahia Blanca"]
# aparatos_tegnologico = ["Arduino UNO", "Sensor de temperatura","Cable USB","Display LCD","Protoboard"]


# menu = True


# matriz_precio = [[120, 100, 100, 312, 2343],
#                  [1200, 100, 100, 312, 234],
#                  [120, 100, 10000, 312, 234],
#                  [120, 100, 100,  3124, 2343]]



# while menu:

#     print("")

#     opcion = int(input("Ingrese una opcion:"))

#     match opcion:
#         case 1:
#             print("selecciones 1:")
#             matriz_precio = inicialisaar_matriz(len(areas), 
#                                          len(aparatos_tegnologico))
            
#             matriz_precio = cargar_matriz_secuencial(matriz_precio)

#             for i in range(len(matriz_precio)):
#                 for j in range(len(matriz_precio[i])):
#                     print(matriz_precio[i][j],end = " ")
#                 print("")

#         case 2:
#             print("selecciones 2:")
#             for i in range(len(matriz_precio)):
#                 for j in range(len(matriz_precio[i])):   
                
#                     if matriz_precio[i][j] > 5000:
#                         print(f"strock que llega a más de 5000 unidades es {areas[i]} con un total {matriz_precio[i][j]} {aparatos_tegnologico[j]} ")
#         case 3:
#             print("selecciones 3:")

#             for i in range(len(matriz_precio)):
#                 # total = 0
#                 for j in range(len(matriz_precio[i])):
#                     # total += matriz_precio[i][j]
                
#                     if matriz_precio[i][j] > 30000:
#                         print(f"strock que llega a más de 30000 unidades es {areas[i]} con un total {matriz_precio[i][j]} {aparatos_tegnologico[j]} ")#


                # nota por que estamos recorriendo insumo(columnas) no filas
#         case 4:
#             print("selecciones 4:")
#             for i in range(len(matriz_precio)):
#                 matriz_max = -1

#                 for j in range(len(matriz_precio[i])):
#                     if matriz_precio[i][j] > matriz_max:
#                         matriz_max = matriz_precio[i][j]

#                 print(f"En que tiene insumo maximo en la zona {areas[i]} tiene {matriz_max} es {aparatos_tegnologico[j]}, ")

#             # indice_max = 0 #
#             # for j in range(len(matriz_precio[i])):
#             #     if matriz_precio[i][j] > matriz_precio[i][indice_max]:
#             #         indice_max = j
#             # print(f"En la zona {areas[i]}, el insumo con más stock es {aparatos_tegnologico[indice_max]} con {matriz_precio[i][indice_max]} unidades.")



#         case 5:
#             print("selecciones 5:")


#         case 6:
#             print("selecciones 6:")

#             oredenamiento = ordenar_burbujeo(matriz_precio)

#             for i in range(len(matriz_precio)):#
#                 ordenar_burbujeo(matriz_precio[i])

#             for i in range(len(oredenamiento)):
#                 for j in range(len(oredenamiento[i])):
#                     print(oredenamiento[i][j],end = " ")
#                 print("")

        

#         case 7:
#             print("selecciones 7:")
#         case 8:
#             print("selecciones 8:")
#         case 9:
#             print("selecciones 9:")
#         case 10:
#             print("Salida")
#             ejecutar_menu = False

#             break
        
#         case _:
#             pass



#  Conclusión


# Concepto	            En la matriz	    Lista relacionada
# Depósitos	            Filas (i)	            areas
# Insumos/productos	    Columnas (j)	    aparatos_tegnologico

