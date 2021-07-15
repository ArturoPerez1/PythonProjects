#Class Definition
class Personas:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def saluda(self, otra_Persona):
        return f'Hola {otra_Persona.nombre}, me llamo {self.nombre}.'

#global variables
arturo = Personas('Arturo', 18)
wilmer = Personas('Wilmer', 26)

 
#saludo
saludo = arturo.saluda(wilmer)
print(saludo)