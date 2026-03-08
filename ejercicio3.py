# ### Ejercicio 3: Herencia y Decoradores
#
# Para este nivel, vamos a combinar la jerarquía de clases (como el ejemplo de **Vehículo/Terrestre/Aéreo** del **29/1/26** ) con el uso de **decoradores** para monitorizar la ejecución (visto el **27/1/26** ).
#
# **Tu tarea:**
# Crea un script llamado `ejercicio3.py` con lo siguiente:
#
# 1.
# **Decorador `log_operacion**`: Crea un decorador que, cada vez que se llame a un método, imprima: `"Executando método: [nome_do_metodo]"`.
#
#
# 2. **Clase Base `ItemBiblioteca**`:
# * Atributos: `codigo` e `titulo`.
# * Método `mostrar_info` (decorado con `@log_operacion`).
#
#
# 3.
# **Clase Filla `Revista**` (hereda de `ItemBiblioteca` ):
#
#
# * Atributos propios: `numero_edicion`.
# * Sobreescribe `mostrar_info` para engadir o número de edición.
#
#
#
#
# 4. **Clase Filla `DVD**` (hereda de `ItemBiblioteca`):
# * Atributos propios: `duracion`.
# * Sobreescribe `mostrar_info`.
#
#
#
# **Obxectivo:** Instancia unha `Revista` e un `DVD`, e chama aos seus métodos para comprobar que o decorador funciona correctamente en ambos.

def log_operacion(func):
    def wrapper(*args, **kwargs):
        print(f"Executando método: {func.__name__}")
        return func(*args, **kwargs)

class ItemBiblioteca:
    def __init__(self,codigo,titulo):
        self.codigo = codigo
        self.titulo = titulo

    @log_operacion
    def mostrar_info(self):
        print(f"Codigo: {self.codigo}, titulo: {self.titulo}")

class Revista(ItemBiblioteca):
    def __init__(self,codigo,titulo,numero_edicion):
        super().__init__(codigo,titulo)
        self.numero_edicion = numero_edicion

    @log_operacion
    def mostrar_info(self):
        print(f"Codigo: {self.codigo}, titulo: {self.titulo}, numero: {self.numero_edicion}")

class DVD(ItemBiblioteca):
    def __init__(self,codigo,titulo,duracion):
        super().__init__(codigo,titulo)
        self.duracion = duracion

    @log_operacion
    def mostrar_info(self):
        print(f"Codigo: {self.codigo}, titulo: {self.titulo}, duracion: {self.duracion}")


revista1 = Revista("R001","Hola!",1)

dvd1 = DVD("DVD001","New Divide",245)

revista1.mostrar_info()
dvd1.mostrar_info()