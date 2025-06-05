#Nombre y Apellido: Junior Camacho 
#Div: 117

from paquetes.matriz import *

#ubicaciones
areas = ["Rosario","Cordoba","Salta","Bahia Blanca"]
aparatos_tegnologico = ["Arduino UNO", "Sensor de temperatura","Cable USB","Display LCD","Protoboard"]


menu = True


matriz_precio = [[120, 100, 100, 312, 2343],
                 [1200, 100, 100, 312, 234],
                 [120, 100, 10000, 312, 234],
                 [120, 100, 100,  3124, 2343]]



while menu:

    print("")

    opcion = int(input("Ingrese una opcion:"))

    match opcion:
        case 1:
            print("selecciones 1:")
            matriz_precio = inicialisaar_matriz(len(areas), 
                                         len(aparatos_tegnologico))
            
            matriz_precio = cargar_matriz_secuencial(matriz_precio)

            for i in range(len(matriz_precio)):
                for j in range(len(matriz_precio[i])):
                    print(matriz_precio[i][j],end = " ")
                print("")

        case 2:
            print("selecciones 2:")
            for i in range(len(matriz_precio)):
                for j in range(len(matriz_precio[i])):   
                
                    if matriz_precio[i][j] > 5000:
                        print(f"strock que llega a más de 5000 unidades es {areas[i]} con un total {matriz_precio[i][j]} {aparatos_tegnologico[j]} ")
        case 3:
            print("selecciones 3:")

            for i in range(len(matriz_precio)):
                # total = 0
                for j in range(len(matriz_precio[i])):
                    # total += matriz_precio[i][j]
                
                    if matriz_precio[i][j] > 30000:
                        print(f"strock que llega a más de 5000 unidades es {areas[i]} con un total {matriz_precio[i][j]} {aparatos_tegnologico[j]} ")



        case 4:
            print("selecciones 4:")
            for i in range(len(matriz_precio)):
                matriz_max = -1

                for j in range(len(matriz_precio[i])):
                    if matriz_precio[i][j] > matriz_max:
                        matriz_max = matriz_precio[i][j]

                print(f"En que tiene insumo maximo en la zona {areas[i]} tiene {matriz_max} es {aparatos_tegnologico[j]}, ")


        case 5:
            print("selecciones 5:")


        case 6:
            print("selecciones 6:")

            oredenamiento = ordenar_burbujeo(matriz_precio)

            for i in range(len(oredenamiento)):
                for j in range(len(oredenamiento[i])):
                    print(oredenamiento[i][j],end = " ")
                print("")
        

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