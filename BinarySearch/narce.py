def binaria(lista, busqueda):
    inicio =0
    fin = len(lista)-1

    while inicio<=fin:
        mitad= round((fin-inicio)/2)+inicio

        adivinar = lista[mitad]

        if adivinar == busqueda:
            return mitad
        elif adivinar > busqueda:
            fin = mitad - 1
        else:
            inicio = mitad + 1

    return None

lista = list(range(1,11))

busqueda = 6

print(binaria(lista, busqueda))
