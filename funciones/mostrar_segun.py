from .ordenar import ordenar_por_max_llave as maxllave
from .ordenar import ordenar_por_min_llave as minllave

def mostrar_completa(lista_diccionarios:list[dict])->None:
    '''Recibe una lista de diccionarios e imprime cada diccionario separado entre corchetes
    ### Args
        lista_diccionario: list[dict]
    ### Returns
        None
    '''
    for elemento in lista_diccionarios:
        print("{")
        for llave, valor in elemento.items():
            print(f"    {llave}: {valor}")
        print("},")

def mostrar_llaves(diccionario: dict)->list[str]:
    '''Recibe un diccionario y devuelve una lista con los nombres de cada una de sus llaves
    ### Args:
        diccionario: dict
    ### Returns
        list[str]
    '''
    lista_llaves = []
    llaves = diccionario.keys()
    
    for llave in llaves:
        lista_llaves += [llave]
    return lista_llaves 

def mostrar_especificas(lista_diccionarios:list[dict] ,lista_llaves: list[str])->list[dict]:
    '''Recibe una lista de diccionarios y una lista de nombres de llaves. 
    Genera una nueva lista de diccionarios con las llaves indicadas en la lista
    ### Args:
        lista_diccionarios: list[dict]
        lista_llave4s: list[str]
    ### Returns:
        list[dict]
    '''
    nuevo_diccionario = {}
    nueva_lista_diccionario = []
    
    for elemento in lista_diccionarios:
        
        for llave in lista_llaves:
            valor = elemento.get(llave)
            nuevos_datos = {llave: valor}
            nuevo_diccionario.update(nuevos_datos)
        
        nueva_lista_diccionario += [nuevo_diccionario]
        nuevo_diccionario = {}
    return nueva_lista_diccionario

def mostrar_maximo_llave(lista_diccionarios:list[dict], llave:str)->list[dict]:
    '''Recibe una lista de diccionarios y el nombre de una llave. 
    Devolvera una lista de los diccionarios con el valor maximo segun la llave
    ### Args:
        lista_diccionarios: list[dict]
        llave: str
    ### Returns:
        list[dict]
    '''
    lista_diccionarios = maxllave(lista_diccionarios, llave)
    lista_maximos = [lista_diccionarios[0]]
    i = 1
    while(lista_diccionarios[0].get(llave) == lista_diccionarios[i].get(llave)):
        lista_maximos += [lista_diccionarios[i]]
        i += 1
        if i == len(lista_diccionarios):
            break
    return lista_maximos

def mostrar_minimo_llave(lista_diccionarios:list[dict], llave:str)->list[dict]:
    '''Recibe una lista de diccionarios y el nombre de una llave. 
    Devolvera una lista de los diccionarios con el valor minimo segun la llave
    ### Args:
        lista_diccionarios: list[dict]
        llave: str
    ### Returns:
        list[dict]
    '''
    lista_diccionarios = minllave(lista_diccionarios, llave)
    lista_maximos = [lista_diccionarios[0]]
    i = 1
    while(lista_diccionarios[0].get(llave) == lista_diccionarios[i].get(llave)):
        lista_maximos += [lista_diccionarios[i]]
        i += 1
        if i == len(lista_diccionarios):
            break
    return lista_maximos