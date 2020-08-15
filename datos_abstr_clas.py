#Definicion de una clase
# class <nombre_de_la_clase>(<super_clase>):
#     def __init__(self,<parametros>):
#         <expresion>

#     def <nombre_del_metodo>(self,<parametros>):
#         <expresion>


###Ejemplo::::

#Definicion
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def saluda(self,otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre}.'

#usando la clase
angel = Persona('Angel',26)
david = Persona('David',35)

print(angel.saluda(david))

    