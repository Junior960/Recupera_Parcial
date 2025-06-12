
# 2
def mostrar_depositos_mayor_5000(matriz, nombres_areas):
    for i in range(len(matriz)):
        total = 0
        for j in range(len(matriz[i])):
            total = total + matriz[i][j]
        if total > 5000:
            print(f"Depósito: {nombres_areas[i]} Stock total: {total}")


# 3
def mostrar_insumos_con_stock_superior(matriz, nombres_insumos, umbral):
    for j in range(len(nombres_insumos)):
        total = 0
        for i in range(len(matriz)):  
            total += matriz[i][j]

        if total > umbral:
            print(f"El insumo {nombres_insumos[j]} tiene un stock total de {total} unidades.\n")

        

# 4

# def mostrar_deposito_maximo_por_insumo(matriz, nombres_areas, nombres_insumos):
#     for j in range(len(nombres_insumos)):  # Recorremos insumos (columnas)
#         maximo = matriz[0][j]

#         # Buscamos el valor máximo
#         for i in range(1, len(nombres_areas)):
#             if matriz[i][j] > maximo:
#                 maximo = matriz[i][j]




