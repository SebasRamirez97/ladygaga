def obtener_numeros(cadena: str)->int:
    '''Recibe una cadena alfanumerica y devuelve 
    los numeros casteados a enteros
    
    ### Args:
        cadena: str
    ### Returns:
        int
    '''
    
    nueva_cadena = ""
    i = 0
    while(i < len(cadena)):
        if cadena[i].isdigit():
            nueva_cadena += cadena[i]
        i+=1
    return int(nueva_cadena)

def promedio_valores_diccionarios(lista_diccionarios: list[dict], llave: str)->int:
    '''Recibe una lista de diccionarios y una llave. 
    Calculara el pormedio de los valores de la llave ingresad y lo devuelve casteado a entero.
    ### Args:
        lista_diccionarios: list[dict]
    ### Returns:
        int 
    '''
    lista_valores = []
    for diccionario in lista_diccionarios:
        lista_valores += [obtener_numeros(diccionario.get(llave))]
    
    promedio = sum(lista_valores) / len(lista_diccionarios)

    return int(promedio)