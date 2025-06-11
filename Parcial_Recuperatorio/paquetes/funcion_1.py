def mostrar_depositos_mayor_5000(matriz, nombres_areas):
    for i in range(len(matriz)):
        total = 0
        for j in range(len(matriz[i])):
            total = total + matriz[i][j]
        if total > 5000:
            print(f"Depósito: {nombres_areas[i]} Stock total:{total}")
        


def mostrar_max_stock_por_insumo(matriz, insumos, depositos):
    resultados = []

    for j in range(len(insumos)):  # Recorre insumos (columnas)
        maximo = matriz[0][j]
        indice_max = 0
        for i in range(1, len(depositos)):  # Recorre depósitos (filas)
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                indice_max = i

        mensaje = f"El insumo {insumos[j]} tiene más stock en {depositos[indice_max]} con {maximo} unidades."
        resultados += [mensaje]

    return resultados


