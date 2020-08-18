#Codigo extraido del siguiente enlace:
#https://recursospython.com/guias-y-manuales/clases-y-orientacion-a-objetos/


#Clases en python

class Estudiante:

    def __init__(self,name,asignaturas):
        if not isinstance(name,str):
            raise TypeError('El nombre debe ser de tipo str')
        elif not isinstance(asignaturas,list):
            raise TypeError('Las asignaturas deben ser una lista')
        self.name = name
        self.asignaturas = asignaturas

    def print_info(self):
        print("Nombre: {}".format(self.name))
        print("Asignaturas: {}".format(self.asignaturas))

student = Estudiante('Pablo',[5,14,3])

student2 = Estudiante('Pedro',[1,9])

# student.print_info()
# student2.print_info()


# Recordemos que ambas llamadas a continuación son equivalentes:
Estudiante.print_info(student)
student.print_info()

# los nombres de instancias se escriben
#  en letras minúsculas y cada palabra
#  separada por guiones bajos.
#  Por el contrario, las clases 
# se nombran sin guiones bajos y
#  poniendo en mayúscula la primera letra
#  de cada palabra

# student.name = 'Pablo'
# student.asignaturas = [5,14,3]
# print(student.name)

# student2 = Estudiante()
# student2.name = 'Pedro'
# student2.asignaturas = [1,9]
