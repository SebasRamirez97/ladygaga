'''diccionario = {"palabra": "coso"}
par = diccionario.items()
nuevo_diccionario = {}
for llave, coso in par:
    nuevos_datos = {llave: coso}
    nuevo_diccionario.update(nuevos_datos)
'''
'''lista = [{
            "Tema": "Colby O'Donis | Akon - Just Dance",
            "Vistas": "300 millones",
            "Duracion": "4:01",
            "Link Youtube": "https://www.youtube.com/watch?v=2Abk1jAONjw",
            "Fecha lanzamiento": "2008-04-08"
        },
]
nuevo_diccionario = {}
lista_llaves =["Tema","Duracion"]
for elemento in lista:
    for llave in lista_llaves:
        valor = elemento.get(llave)
        nuevos_datos = {llave: valor}
        nuevo_diccionario.update(nuevos_datos)

print(nuevo_diccionario)
'''
lista_diccionarios = [
        {
            "Tema": "Colby O'Donis | Akon - Just Dance",
            "Vistas": "300 millones",
            "Duracion": "4:01",
            "Link Youtube": "https://www.youtube.com/watch?v=2Abk1jAONjw",
            "Fecha lanzamiento": "2008-04-08"
        },
        {
            "Tema": "Poker Face",
            "Vistas": "1200 millones",
            "Duracion": "3:57",
            "Link Youtube": "https://www.youtube.com/watch?v=bESGLojNYSo",
            "Fecha lanzamiento": "2008-09-26"
        }]
'''nuevo_diccionario = {}
nueva_lista_diccionario = []
lista_llaves =["Tema","Duracion"]
for elemento in lista_diccionarios:
        
    for llave in lista_llaves:
        valor = elemento.get(llave)
        nuevos_datos = {llave: valor}
        nuevo_diccionario.update(nuevos_datos)
        
    nueva_lista_diccionario += [nuevo_diccionario]
    nuevo_diccionario = {}
print(nueva_lista_diccionario)'''

for i in range (len(lista_diccionarios)):
    for j in range(len(lista_diccionarios)-i-1):
        if lista_diccionarios[j].get("Duracion") < lista_diccionarios[j+1].get("Duracion"):
            aux = lista_diccionarios[j+1]
            lista_diccionarios[j+1] = lista_diccionarios[j]
            lista_diccionarios[j] = aux

print(lista_diccionarios)
