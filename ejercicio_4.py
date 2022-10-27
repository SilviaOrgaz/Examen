class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Se ha creado con exito")
    
    def __str__(self):
        return "El alumno {} ha sacado una nota de {}".format(self.nombre, self.nota)
        

    def calificacion(self):
        if self.nota <= 5:
            print("El alumno {} ha suspendido con una nota de {}".format(self.nombre, self.nota))
        else:
            print("El alumno {} ha aprobado con una nota de {}".format(self.nombre, self.nota))

A = Alumno("Silvia", 4)
B = Alumno("Cristina", 9)
A.calificacion()
B.calificacion()