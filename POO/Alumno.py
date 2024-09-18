

class Alumno:
    def __init__(self, apellido, nombre):
        self.apellido = apellido
        self.nombre = nombre
 
    def saludar(self):
        print (f"Hola mi nombre es {self.nombre} que tengas un buen día")
        
    def adios(self):
        print (f"Me despido {self.nombre}")
    def __str__(self):
        return self.nombre + " "+ self.apellido