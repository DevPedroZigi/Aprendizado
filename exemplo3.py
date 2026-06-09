def filtrar_pares(lista):
    lista_pares = []
    for item in lista:
        if item % 2 == 0:
            lista_pares.append(item)
    return lista_pares


# programa principal
lista = [1 ,4 ,7, 10, 13, 16, 19, 22]
lista_pares = filtrar_pares(lista)
print(lista_pares)
