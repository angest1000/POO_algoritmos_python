class Persona:

    def __init__(self, nombre='', apellido_paterno='', apellido_materno='', edad=0, sexo=None):
        self._nombre = nombre
        self._apellido_paterno = apellido_paterno
        self._apellido_materno = apellido_materno
        self._edad = edad
        self._sexo = sexo

    '''nombre getter and  setter'''
    @property
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    '''apellido_paterno getter and  setter'''
    @property
    def get_apellido_paterno(self):
        return self._apellido_paterno

    def set_apellido_paterno(self, apellido_paterno):
        self._apellido_paterno = apellido_paterno

    '''apellido_materno getter and  setter'''
    @property
    def get_apellido_materno(self):
        return self._apellido_materno

    def set_apellido_materno(self, apellido_materno):
        self._apellido_materno = apellido_materno

    '''Edad getter and setter'''
    @property
    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    '''Sexo getter and setter'''
    @property
    def get_sexo(self):
        return self._sexo

    def set_sexo(self, sexo):
        self._sexo = sexo

print('Ingresa tu informacion a continuacion: ')

input_nombre = input('Ingresa tu nombre: ')
input_apellido_paterno = input('Ingresa tu apellido paterno: ')
input_apellido_materno = input('Ingresa tu apellido materno: ')
input_edad = int(input('Ingresa tu Edad: '))
input_sexo = input('Ingresa tu Sexo: ')

persona = Persona()
persona.set_nombre(input_nombre)
persona.set_apellido_paterno(input_apellido_paterno)
persona.set_apellido_materno(input_apellido_materno)
persona.set_edad(input_edad)
persona.set_sexo(input_sexo)

print(f'Confirma tu informacion, tu nombre son: {persona.get_nombre} {persona.get_apellido_paterno} {persona.get_apellido_materno} con edad: {persona.get_edad} y sexo: {persona.get_sexo}')
