#Prueba de carga de paises
from funciones import (
    cargar_paises,
    agregar_pais,
    actualizar_pais,
    buscar_pais,
    filtrar_continente,
    ordenar_nombre,
    mayor_poblacion,
    menor_poblacion,
    promedio_poblacion,
    promedio_superficie,
    cantidad_continentes
)

paises =  cargar_paises()

print(paises)

#Menu
while True:

    print("\nGestion de Paises")
    print("1. Agregar")
    print("2. Actualizar")
    print("3. Buscar")
    print("4. Filtrar continente")
    print("5. Ordenar nombre")
    print("6. Estadisticas")
    print("7. Salir")

    opcion = input("Opcion: ").strip()

    if opcion == "":

        print("Error. Debe ingresar una opcion.")
        continue

    elif not opcion.isdigit():

        print("Error. Debe ingresar un número.")
        continue


    if opcion == "1":

        agregar_pais(paises)

    elif opcion == "2":

        actualizar_pais(paises)

    elif opcion == "3":

        buscar_pais(paises)

    elif opcion == "4":

        filtrar_continente(paises)

    elif opcion == "5":

        ordenar_nombre(paises)

    elif opcion == "6":

        print("\nMayor poblacion:")
        mayor_poblacion(paises)

        print("\nMenor poblacion:")
        menor_poblacion(paises)

        print("\nPromedio poblacion:")
        promedio_poblacion(paises)

        print("\nPromedio superficie:")
        promedio_superficie(paises)

        print("\nCantidad por continente:")
        cantidad_continentes(paises)

    elif opcion == "7":

        print("Programa finalizado")
        break

    else:

        print("La opcion debe estar entre 1 y 7.")