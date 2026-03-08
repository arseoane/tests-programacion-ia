# Ejercicio 2: Persistencia en Ficheros (CSV)
#
# Ahora que dominas las validaciones, vamos a dar un paso más integrando lo aprendido el 20/1/26 y el 3/3/26 sobre manejo de archivos.
#
# **Tu tarea:**
# Crea un script llamado `ejercicio2.py` que realice lo siguiente:
#
# 1. **Clase `Libro` mejorada:** Usa la clase del ejercicio anterior.
# 2. **Carga de datos:** Al iniciar, el programa debe leer un archivo llamado `biblioteca.csv`. Si el archivo no existe, debe crearlo con la cabecera: `titulo,autor,paginas`.
#
#
# 3. **Menú interactivo:**
# * 1. Engadir libro: Pide los datos al usuario, crea el objeto `Libro` (validando los datos) y guárdalo en una nueva línea del CSV.
#
#
# * 2. Listar libros: Lee el CSV y muestra por pantalla todos los libros guardados.
#
#
# * **3. Saír.**
#
#
#
# **Dato importante:** Recuerda usar el bloque `try-except` al abrir archivos para gestionar el error si el fichero no existe inicialmente.

from ejercicio1 import Libro
import csv


try:
    with open("biblioteca.csv","r") as biblioteca:
        next(biblioteca)
        csvreader = csv.reader(biblioteca)

    while True:
        print("=" * 20)
        print("1. Engadir libro.")
        print("2. Listar libros.")
        print("3. Saír.")

        opcion = int(input("\nSelecciona una opción: "))
        print("=" * 20)

        match opcion:
            case 1:
                with open("biblioteca.csv", "a") as biblioteca:
                    writer = csv.writer(biblioteca)
                    writer.writerow([input("Título: "), input("Autor: "), int(input("Páginas: "))])

            case 2:
                with open("biblioteca.csv", "r") as biblioteca:
                    next(biblioteca)
                    for libro in biblioteca:
                        print(libro)

            case 3:
                break

            case _:
                print("Opción inválida.")



except FileNotFoundError:
    with open("biblioteca.csv","w") as biblioteca:
        csvwriter = csv.writer(biblioteca)
        csvwriter.writerow(["titulo","autor","paginas"])

except Exception as e:
    print(f"El siguiente error ha ocurrido: '{e}'.")