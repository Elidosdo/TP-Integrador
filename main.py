import csv

with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
    escritor.writerow(["Argentina", 45376763, 2780400, "América"])
    escritor.writerow(["Japón", 125800000, 377975, "Asia"])
    escritor.writerow(["Brasil", 213993437, 8515767, "América"])
    escritor.writerow(["Alemania", 83149300, 357022, "Europa"])

print("CSV creado")