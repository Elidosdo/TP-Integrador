import csv
import os
#Cargar paises
def cargar_paises():

    paises = []

    ruta_csv = os.path.join(
        os.path.dirname(__file__),
        "paises.csv"
    )

    try:

        with open(ruta_csv, "r", encoding="utf-8") as archivo:

            lector = csv.DictReader(archivo)

            for fila in lector:

                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }

                paises.append(pais)

    except FileNotFoundError:

        print("Archivo no encontrado")

    return paises

#Guardar Paises
def guardar_paises(paises):

    ruta_csv = os.path.join(
        os.path.dirname(__file__),
        "paises.csv"
    )

    with open(
        ruta_csv,
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo:

        campos = [
            "nombre",
            "poblacion",
            "superficie",
            "continente"
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=campos
        )

        escritor.writeheader()

        escritor.writerows(paises)

#Agregar paises
def agregar_pais(paises):

    while True:

        nombre = input("Nombre: ").strip()

        if nombre == "":

            print("Error. No se permiten campos vacíos.")
        
        elif len(nombre) < 2:

            print("El nombre es demasiado corto.")

        elif not nombre.replace(" ", "").isalpha():

            print("Error. Solo se permiten letras.")

        else:

            repetido = False

            for pais in paises:

                if pais["nombre"].lower() == nombre.lower():

                    repetido = True
                    break 
            
            if repetido:

                print("Ese país ya existe.")


            else:

             break

    while True:

        try:

            poblacion = int(
                input("Poblacion: ")
            )

            if poblacion > 0:
                break

            print("Debe ser mayor que cero.")
        
        except ValueError:

            print("Ingrese números.")

    while True:

        try:

            superficie = int(
                input("Superficie: ")
            )

            if superficie > 0:
                break

            print("Debe ser mayor a cero.")

        except ValueError:

            print("Ingrese números.")
    
    while True:

        continente = input(
            "Continente: "
        ).strip()

        if continente == "":

            print("No se permiten vacíos.")

        elif not continente.replace(" ", "").isalpha():

            print("Solo letras.")

        else:

            break

    nombre = nombre.title()
    continente = continente.title()
    pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(pais)

    guardar_paises(paises)

    print(f"Pais '{nombre}' agregado correctamente.")

#Actualizar paises
def actualizar_pais(paises):

    while True:

        nombre = input("Pais a actualizar: ").strip()

        if nombre == "":

            print("No se permiten vacios.")

        elif not nombre.replace(" ", "").isalpha():

            print("Solo letras.")

        else:

            break

    for pais in paises:

        if pais["nombre"].lower() == nombre.lower():

            while True:

                try:

                    nueva_poblacion = int(
                        input("Nueva poblacion: ")
                    )

                    if nueva_poblacion <= 0:

                        print("Debe ser mayor que cero.")

                    else:

                        break

                except ValueError:

                    print("Ingrese solo numeros.")

            while True:

                try:

                    nueva_superficie = int(
                        input("Nueva superficie: ")
                    )

                    if nueva_superficie <= 0:

                        print("Debe ser mayor que cero.")

                    else:

                        break

                except ValueError:

                    print("Ingrese solo numeros.")

            pais["poblacion"] = nueva_poblacion
            pais["superficie"] = nueva_superficie

            guardar_paises(paises)

            print("Pais actualizado correctamente.")

            return

    print("Pais no encontrado.")

#Buscar paises
def buscar_pais(paises):

    while True:

        texto = input("Buscar: ").strip().lower()

        if texto == "":

            print("No se permiten vacios.")

        elif not texto.replace(" ", "").isalpha():

            print("Solo letras.")

        else:

            break

    encontrados = []

    for pais in paises:

        if texto in pais["nombre"].lower():

            encontrados.append(pais)

    if len(encontrados) == 0:

        print("Sin resultados")

    else:

        for pais in encontrados:

            print(
            f"Nombre: {pais['nombre']} | "
            f"Poblacion: {pais['poblacion']} | "
            f"Superficie: {pais['superficie']} | "
            f"Continente: {pais['continente']}"
            )

#Filtrar continente
def filtrar_continente(paises):

    while True:

        continente = input(
            "Continente: "
        ).strip().lower()

        if continente == "":

            print("No se permiten vacios.")

        elif not continente.replace(" ", "").isalpha():

            print("Solo letras.")

        else:

            break

    encontrados = False

    for pais in paises:

        if pais["continente"].lower() == continente:

            print(pais)
            encontrados = True

    if not encontrados:

        print("No se encontraron paises en ese continente.")

#Ordenar nombre
def ordenar_nombre(paises):

    if len(paises) == 0:

        print("No hay paises cargados.")
        return

    ordenados = sorted(
        paises,
        key=lambda pais: pais["nombre"]
    )

    for pais in ordenados:

        print(pais)

#Estadisticas
def mayor_poblacion(paises):

    if len(paises) == 0:

        print("No hay paises cargados.")
        return

    pais = max(
        paises,
        key=lambda p: p["poblacion"]
    )

    print(
        f"Pais con mayor poblacion: {pais['nombre']} "
        f"({pais['poblacion']} habitantes)"
    )

def menor_poblacion(paises):
    
    if len(paises) == 0:

        print("No hay paises cargados.")
        return

    pais = min(
        paises,
        key=lambda p: p["poblacion"]
    )

    print(
    f"Pais con menor poblacion: {pais['nombre']} "
    f"({pais['poblacion']} habitantes)"
)

def promedio_poblacion(paises):

    if len(paises) == 0:

        print("No hay paises cargados.")
        return

    total = 0

    for pais in paises:

        total += pais["poblacion"]

    promedio = total / len(paises)

    print(
    f"Promedio de poblacion: {promedio:.2f}"
)

def cantidad_continentes(paises):

    if len(paises) == 0:

        print("No hay paises cargados.")
        return

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:

            continentes[continente] += 1

        else:

            continentes[continente] = 1

    for continente, cantidad in continentes.items():

        print(
        f"{continente}: {cantidad} pais(es)"
        )

def promedio_superficie(paises):

    if len(paises) == 0:

        print("No hay paises cargados.")
        return

    total = 0

    for pais in paises:

        total += pais["superficie"]

    promedio = total / len(paises)

    print(
        f"Promedio de superficie: {promedio:.2f} km²"
    )