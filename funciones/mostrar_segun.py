
def mostrar_completa(lista_diccionarios):
    

    for elemento in lista_diccionarios:
        print("{")
        for llave, valor in elemento.items():
            print(f"    {llave}: {valor}")
        print("},")


def mostrar_llaves(diccionario):
    lista_llaves = []
    llaves = diccionario.keys()
    
    for llave in llaves:
        lista_llaves += [llave]
    return lista_llaves 


def mostrar_especificas(lista_diccionarios ,lista_llaves):
    
    nuevo_diccionario = {}
    nueva_lista_diccionario = []
    
    for elemento in lista_diccionarios:
        
        for llave in lista_llaves:
            valor = elemento.get(llave)
            nuevos_datos = {llave: valor}
            nuevo_diccionario.update(nuevos_datos)
        
        nueva_lista_diccionario += [nuevo_diccionario]
        nuevo_diccionario = {}
    mostrar_completa(nueva_lista_diccionario)