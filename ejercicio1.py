class Libro:
    def __init__(self, titulo, autor, paginas):
        if titulo == "":
            raise ValueError("El título no puede estar vacío.")
        else:
            self.titulo = titulo

        if autor == "":
            raise ValueError("El autor no puede estar vacío.")
        else:
            self.autor = autor

        if type(paginas) != int:
            raise TypeError("El número de páginas debe ser INT.")
        elif paginas <= 0:
            raise ValueError("Un libro debe tener al menos una página.")
        else:
            self.paginas = paginas


    def __str__(self):
        return f"Libro: {self.titulo} - Autor: {self.autor} ({self.paginas} págs)"


