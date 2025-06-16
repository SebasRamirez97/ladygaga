from funciones.listita import lista_temas as temas
from funciones.mostrar_segun import mostrar_completa as completa
from funciones.mostrar_segun import mostrar_llaves as llaves
from funciones.mostrar_segun import mostrar_especificas as especificas
from funciones.mostrar_segun import mostrar_maximo_llave as getmax
from funciones.mostrar_segun import mostrar_minimo_llave as getmin
from funciones.ordenar import ordenar_por_max_llave as ordmax
from funciones.calculos import promedio_valores_diccionarios as promedio
opcion = 0
while opcion != 9:
    print("MENU PRINCIPAL")
    print(
        "1. Mostrar lista de temas.\n"
        "2. Ordenar temas por duracion.\n"
        "3. Promedio de vistas.\n"
        "4. Maxima reproduccion.\n"
        "5. Minima reproduccion\n"
        "6. Busqueda por codigo.\n"
        "7. Listar por colaborador.\n"
        "8. Listar por mes de lanzamineto.\n"
        "9. Salir."
    )

    opcion = int(input("Seleccione una opcion: "))

    match opcion:
        case 1:
            print(llaves(temas()[0]))
            completa(especificas(temas(),["Tema","Duracion"]))
        case 2:
            completa(ordmax(temas(), "Duracion"))
        case 3:
            print(f"{promedio(temas(), "Vistas")} millones")
        case 4:
            completa(getmax(temas(),"Vistas"))
        case 5:
            completa(getmin(temas(),"Vistas"))
        case 6:
            pass
        case 7:
            pass
        case 8:
            pass
        case 9:
            print("Finalizando la sesion.")
        case _:
            print("No es un valor correcto de los indicados.")
        
