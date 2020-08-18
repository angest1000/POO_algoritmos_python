#Codigo extraido del siguiente enlace:
#https://recursospython.com/guias-y-manuales/clases-y-orientacion-a-objetos/


#Clases en python

class Estudiante:

    def __init__(student,name,asignaturas):
        if not isinstance(name,str):
            raise TypeError('El nombre debe ser de tipo str')
        elif not isinstance(asignaturas,list):
            raise TypeError('Las asignaturas deben ser una lista')
        student.name = name
        student.asignaturas = asignaturas

    def print_info(student):
        print("Nombre: {}".format(student.name))
        print("Asignaturas: {}".format(student.asignaturas))

student = Estudiante('Pablo',[5,14,3])

student2 = Estudiante('Pedro',[1,9])

student.print_info()
student2.print_info()

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
