import csv

with open("paises.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "poblacion", "superficie", "continente"])
    escritor.writerow(["Argentina", 45376763, 2780400, "América"])
    escritor.writerow(["Japón", 125800000, 377975, "Asia"])
    escritor.writerow(["Brasil", 213993437, 8515767, "América"])
    escritor.writerow(["Alemania", 83149300, 357022, "Europa"])

print("CSV creado")

def cargar_menu():
    while True:
        try:
            print("=== Gestion de paises ===")
            print("1) Agregar pais")
            print("2) Actualizar pais")
            print("3) Buscar pais")
            print("4) Filtrar paises")
            print("5) Ordenar paises")
            print("6) Estadisticas")
            print("7) Salir")
            
            opcion = input("Selecciona una opcion: ")
            opcion = int(opcion)
        except ValueError:
            print("Debe ingresar numeros") 
        else:
            if opcion == "":
                print("No se permiten vacios")

            if opcion == 1:
                pass
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                pass
            elif opcion == 7:
                print("Cerrando programa...")
                break
            else:
                print("Ingrese una opcion valida")
cargar_menu()
