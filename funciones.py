import csv
import os

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