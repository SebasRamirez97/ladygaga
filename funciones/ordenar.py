from .mostrar_segun import mostrar_completa
def ordenar_por_duracion(lista_diccionarios):
    for i in range (len(lista_diccionarios)):
        for j in range(len(lista_diccionarios)-i-1):
            if lista_diccionarios[j].get("Duracion") < lista_diccionarios[j+1].get("Duracion"):
                aux = lista_diccionarios[j+1]
                lista_diccionarios[j+1] = lista_diccionarios[j]
                lista_diccionarios[j] = aux
    mostrar_completa(lista_diccionarios)