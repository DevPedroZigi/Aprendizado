def filtrar_pares(lista):
    lista_pares = []
    for item in lista:
        if item % 2 == 0:
            lista_pares.append(item)
    return lista_pares
