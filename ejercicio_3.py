class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "El nombre del alumno es {} y su nota es de {}".format(self.nombre, self.nota)
        