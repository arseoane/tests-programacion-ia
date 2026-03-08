# Excepción Personalizada: Crea una clase StockInvalidoError que reciba el nombre del producto y el stock intentado.
#
# Clase Componente:
#
# Atributos: nombre, categoria y stock.
#
# En el setter de stock, si el valor es negativo, lanza StockInvalidoError.
#
# Persistencia en JSON:
#
# Crea una función gardar_inventario(lista_obxectos) que convierta los objetos a un diccionario y los guarde en inventario.json usando json.dump.
#
# Crea una función cargar_inventario() que lea el archivo y reconstruya la lista de objetos usando json.load.
#
# Lógica Principal:
#
# Crea un par de componentes.
#
# Intenta asignar un stock negativo dentro de un bloque try-except para capturar tu error personalizado.
#
# Guarda los datos válidos y muéstralos por consola.

import json


class Componente:
    def __init__(self,nombre,categoria,stock):
        self.nombre = nombre
        self.categoria = categoria

        if stock < 0:
            raise StockInvalidoError(nombre,stock)
        else:
            self.stock = stock

    def guardar_inventario(self):
        with open("inventario.json","a") as file:
            json.dump({"nombre":self.nombre,"categoria":self.categoria,"stock":self.stock},file)

    def cargar_inventario(self):
        with open("inventario.json","r") as file:
            inventario = json.load(file)


class StockInvalidoError(Exception):
    def __init__(self, nombre, stock):
        self.nombre = nombre
        self.stock = stock
        pass

    def __str__(self):
        print(f"Error en {self.nombre} con stock {self.stock}.")


try:
    componente1 = Componente("Componente 1","Componentes",1)
    componente2 = Componente("Componente 2","Componentes",-2)

except StockInvalidoError as e:
    print(e)
