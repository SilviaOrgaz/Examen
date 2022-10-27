class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def __str__(self):
        return "El nombre del alumno es {} y su nota es de {}".format(self.nombre, self.nota)

    def calificacion(self):
        if self.nota <= 5:
            print("El alumno {} ha suspendido con una nota de {}".format(self.nombre, self.nota))
        else:
            print("El alumno {} ha aprobado con una nota de {}".format(self.nombre, self.nota))

A = Alumno("Silvia", 4)
B = Alumno("Cristina", 9)
print(A)
print(B)
A.calificacion()
B.calificacion()

