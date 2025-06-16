from .calculos import obtener_numeros

def ordenar_por_max_llave(lista_diccionarios: list[dict], llave: str)->list[dict]:
    '''Recibe una lista de diccionarios y el nombre de una llave. 
    Ordenara los diccionarios de manera descendente segun el valor de la llave y lo retornara.
    ### Args:
        lista_diccionarios: list[dict]
        llave: str
    ### Returns:
        list[dict]
    '''
    for i in range (len(lista_diccionarios)):
        for j in range(len(lista_diccionarios)-i-1):
            if obtener_numeros(lista_diccionarios[j].get(llave)) < obtener_numeros(lista_diccionarios[j+1].get(llave)):
                aux = lista_diccionarios[j+1]
                lista_diccionarios[j+1] = lista_diccionarios[j]
                lista_diccionarios[j] = aux
    return lista_diccionarios

def ordenar_por_min_llave(lista_diccionarios: list[dict], llave: str)->list[dict]:
    '''Recibe una lista de diccionarios y el nombre de una llave. 
    Ordenara los diccionarios de manera ascendente segun el valor de la llave y lo retronara.
    ### Args:
        lista_diccionarios: list[dict]
        llave: str
    ### Returns:
        list[dict]
    '''
    for i in range (len(lista_diccionarios)):
        for j in range(len(lista_diccionarios)-i-1):
            if obtener_numeros(lista_diccionarios[j].get(llave)) > obtener_numeros(lista_diccionarios[j+1].get(llave)):
                aux = lista_diccionarios[j+1]
                lista_diccionarios[j+1] = lista_diccionarios[j]
                lista_diccionarios[j] = aux
    return lista_diccionarios