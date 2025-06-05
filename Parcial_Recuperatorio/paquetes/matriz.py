def inicialisaar_matriz(filas:int, columnas:int, valor:any = 0)-> list :
    matriz = []
    for i in range(filas):
        filas = [valor] * columnas
        matriz += [filas]

    return matriz 

def cargar_matriz_secuencial(matriz_secuencial:list) -> list:
    for i in range(len(matriz_secuencial)):
        for j in range(len(matriz_secuencial[i])):
            matriz_secuencial[i][j] = int(input(f"ingrese un numero en la fila {i} columan {j}: "))

    return matriz_secuencial

def ordenar_burbujeo(lista:list):

    numero = len(lista)
    
    for i in range(numero):
        
        bandera_intercambio = False

        for j in range(0, numero - i - 1):

            if lista [j] > lista[j + 1]:
                bandera_intercambio = True
                menor = lista[j + 1]

                lista[j + 1] = lista[j]
                lista[j] = menor


        if bandera_intercambio == False:
            break


    return lista
            

