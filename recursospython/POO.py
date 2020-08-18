#Codigo extraido del siguiente enlace:
#https://recursospython.com/guias-y-manuales/clases-y-orientacion-a-objetos/


#Clases en python

class Estudiante:

    def __init__(self,name,asignaturas):
        self.set_name(name)
        self.set_asignaturas(asignaturas)

    def set_name(self,name):
        if not isinstance(name,str):
            raise TypeError('El nombre debe ser de tipo str')
        self.name = name

    def get_name(self):
        return self.name

    def set_asignaturas(self,asignaturas):
        if not isinstance(asignaturas,list):
            raise TypeError('Las asignaturas deben ser una lista')
        self.asignaturas = asignaturas

    def get_asignaturas(self):
        return self.asignaturas

    # def print_info(self):
    #     print("Nombre: {}".format(self.name))
    #     print("Asignaturas: {}".format(self.asignaturas))

student = Estudiante('Pablo',[5,14,3])
print(student.name)
print(student.asignaturas)

# student.set_name(1)
student.set_asignaturas('pedro')

# student2 = Estudiante('Pedro',[1,9])

# Recordemos que ambas llamadas a continuación son equivalentes:
# Estudiante.print_info(student)
# student.print_info()

# student.print_info()
# student2.print_info()

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
