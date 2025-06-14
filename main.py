from funciones.listita import lista_temas as temas
from funciones.mostrar_segun import mostrar_llaves as llaves
from funciones.mostrar_segun import mostrar_especificas as especificas
from funciones.ordenar import ordenar_por_duracion as duracion


#completa(temas())
#especificas(temas(),["Tema","Duracion"])
#duracion(temas())
print(llaves(temas()[0]))